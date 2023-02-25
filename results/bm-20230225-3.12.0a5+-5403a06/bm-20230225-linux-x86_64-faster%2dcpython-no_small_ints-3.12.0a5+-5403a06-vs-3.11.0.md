
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_small_ints
- machine: linux-x86_64
- commit hash: 5403a06
- commit date: 2023-02-25
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                      |
| chameleon      | 6.38 ms                                                | 6.46 ms: 1.01x slower                                                     |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                    |
| html5lib       | 64.8 ms                                                | 61.4 ms: 1.06x faster                                                     |
| tornado_http   | 96.5 ms                                                | 94.6 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                                      |
| float          | 76.8 ms                                                | 74.9 ms: 1.03x faster                                                     |
| nbody          | 90.0 ms                                                | 96.1 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.9 ms: 1.02x faster                                                     |
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                                      |
| regex_dna      | 203 ms                                                 | 206 ms: 1.01x slower                                                      |
| regex_effbot   | 3.46 ms                                                | 3.69 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.28 ms: 1.33x faster                                                     |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                      |
| json_loads           | 26.1 us                                                | 23.5 us: 1.11x faster                                                     |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                      |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 99.2 ms: 1.05x faster                                                     |
| pickle_dict          | 31.2 us                                                | 31.5 us: 1.01x slower                                                     |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                     |
| xml_etree_process    | 53.7 ms                                                | 55.0 ms: 1.02x slower                                                     |
| pickle_list          | 4.14 us                                                | 4.25 us: 1.02x slower                                                     |
| xml_etree_generate   | 75.9 ms                                                | 80.6 ms: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.07 ms: 1.06x slower                                                     |
| python_startup_no_site | 6.04 ms                                                | 6.57 ms: 1.09x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.0 ms: 1.10x faster                                                     |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                     |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                     |
| django_template | 32.3 ms                                                | 33.3 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-faster%2dcpython-no_small_ints-3.12.0a5+-5403a06 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.8 ms: 2.38x faster                                                     |
| asyncio_tcp             | 883 ms                                                 | 500 ms: 1.77x faster                                                      |
| json_dumps              | 12.4 ms                                                | 9.28 ms: 1.33x faster                                                     |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                      |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                     |
| richards                | 46.1 ms                                                | 41.4 ms: 1.11x faster                                                     |
| json_loads              | 26.1 us                                                | 23.5 us: 1.11x faster                                                     |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.10x faster                                                     |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                      |
| coroutines              | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                     |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                                      |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                    |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                     |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                                     |
| html5lib                | 64.8 ms                                                | 61.4 ms: 1.06x faster                                                     |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                      |
| logging_silent          | 98.0 ns                                                | 93.4 ns: 1.05x faster                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 99.2 ms: 1.05x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                    |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                     |
| sqlglot_optimize        | 52.7 ms                                                | 50.5 ms: 1.04x faster                                                     |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                      |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                                      |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 787 us: 1.04x faster                                                      |
| pprint_safe_repr        | 706 ms                                                 | 681 ms: 1.04x faster                                                      |
| logging_simple          | 6.02 us                                                | 5.81 us: 1.04x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                     |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                                      |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                      |
| scimark_sor             | 115 ms                                                 | 111 ms: 1.03x faster                                                      |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                     |
| float                   | 76.8 ms                                                | 74.9 ms: 1.03x faster                                                     |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                     |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                     |
| tornado_http            | 96.5 ms                                                | 94.6 ms: 1.02x faster                                                     |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                    |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                     |
| regex_v8                | 22.2 ms                                                | 21.9 ms: 1.02x faster                                                     |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                      |
| logging_format          | 6.48 us                                                | 6.37 us: 1.02x faster                                                     |
| scimark_fft             | 325 ms                                                 | 321 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.52 ms: 1.01x faster                                                     |
| nqueens                 | 83.8 ms                                                | 82.9 ms: 1.01x faster                                                     |
| hexiom                  | 6.34 ms                                                | 6.27 ms: 1.01x faster                                                     |
| create_gc_cycles        | 1.52 ms                                                | 1.50 ms: 1.01x faster                                                     |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                    |
| regex_compile           | 136 ms                                                 | 135 ms: 1.01x faster                                                      |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                      |
| gc_traversal            | 3.82 ms                                                | 3.83 ms: 1.00x slower                                                     |
| mdp                     | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                    |
| async_tree_cpu_io_mixed | 736 ms                                                 | 743 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 68.0 ms                                                | 68.7 ms: 1.01x slower                                                     |
| regex_dna               | 203 ms                                                 | 206 ms: 1.01x slower                                                      |
| pickle_dict             | 31.2 us                                                | 31.5 us: 1.01x slower                                                     |
| fannkuch                | 384 ms                                                 | 389 ms: 1.01x slower                                                      |
| chameleon               | 6.38 ms                                                | 6.46 ms: 1.01x slower                                                     |
| telco                   | 6.43 ms                                                | 6.52 ms: 1.01x slower                                                     |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                     |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                     |
| xml_etree_process       | 53.7 ms                                                | 55.0 ms: 1.02x slower                                                     |
| pickle_list             | 4.14 us                                                | 4.25 us: 1.02x slower                                                     |
| django_template         | 32.3 ms                                                | 33.3 ms: 1.03x slower                                                     |
| chaos                   | 68.7 ms                                                | 70.8 ms: 1.03x slower                                                     |
| crypto_pyaes            | 75.7 ms                                                | 78.4 ms: 1.04x slower                                                     |
| pyflate                 | 419 ms                                                 | 435 ms: 1.04x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                                     |
| python_startup          | 8.58 ms                                                | 9.07 ms: 1.06x slower                                                     |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                     |
| xml_etree_generate      | 75.9 ms                                                | 80.6 ms: 1.06x slower                                                     |
| nbody                   | 90.0 ms                                                | 96.1 ms: 1.07x slower                                                     |
| regex_effbot            | 3.46 ms                                                | 3.69 ms: 1.07x slower                                                     |
| spectral_norm           | 98.1 ms                                                | 105 ms: 1.07x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 670 ms: 1.07x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.57 ms: 1.09x slower                                                     |
| async_generators        | 356 ms                                                 | 422 ms: 1.19x slower                                                      |
| dask                    | 365 ms                                                 | 506 ms: 1.39x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (12): sqlalchemy_imperative, unpickle, go, async_tree_none, djangocms, unpickle_list, bench_mp_pool, sympy_sum, thrift, coverage, scimark_lu, unpack_sequence
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
