
# Results vs. 3.11.0

- fork: faster-cpython
- ref: pep_669_incremental
- machine: linux-x86_64
- commit hash: 5629a3e
- commit date: 2023-02-17
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 244 ms: 1.06x faster                                                            |
| chameleon      | 6.47 ms                                                | 6.33 ms: 1.02x faster                                                           |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                          |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                           |
| tornado_http   | 96.3 ms                                                | 93.3 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.4 ms: 1.07x faster                                                           |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                            |
| nbody          | 93.1 ms                                                | 92.4 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                 | 125 ms: 1.10x faster                                                            |
| regex_effbot   | 3.99 ms                                                | 3.65 ms: 1.09x faster                                                           |
| regex_dna      | 204 ms                                                 | 205 ms: 1.00x slower                                                            |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.37 ms: 1.34x faster                                                           |
| unpickle_pure_python | 228 us                                                 | 193 us: 1.18x faster                                                            |
| json_loads           | 26.5 us                                                | 23.7 us: 1.12x faster                                                           |
| pickle_pure_python   | 306 us                                                 | 279 us: 1.10x faster                                                            |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                            |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                           |
| xml_etree_process    | 53.9 ms                                                | 55.0 ms: 1.02x slower                                                           |
| pickle               | 10.1 us                                                | 10.3 us: 1.03x slower                                                           |
| pickle_list          | 4.11 us                                                | 4.25 us: 1.03x slower                                                           |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.03x slower                                                           |
| xml_etree_generate   | 76.2 ms                                                | 80.3 ms: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.97 ms: 1.05x slower                                                           |
| python_startup_no_site | 6.01 ms                                                | 6.52 ms: 1.09x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.0 ms: 1.13x faster                                                           |
| genshi_text     | 21.6 ms                                                | 20.6 ms: 1.05x faster                                                           |
| mako            | 10.1 ms                                                | 9.76 ms: 1.03x faster                                                           |
| django_template | 32.6 ms                                                | 33.1 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.8 ms: 2.39x faster                                                           |
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                                            |
| json_dumps              | 12.6 ms                                                | 9.37 ms: 1.34x faster                                                           |
| mypy2                   | 420 ms                                                 | 325 ms: 1.29x faster                                                            |
| coroutines              | 25.5 ms                                                | 21.1 ms: 1.21x faster                                                           |
| unpickle_pure_python    | 228 us                                                 | 193 us: 1.18x faster                                                            |
| deltablue               | 3.67 ms                                                | 3.13 ms: 1.17x faster                                                           |
| genshi_xml              | 51.8 ms                                                | 46.0 ms: 1.13x faster                                                           |
| gc_traversal            | 4.02 ms                                                | 3.59 ms: 1.12x faster                                                           |
| json_loads              | 26.5 us                                                | 23.7 us: 1.12x faster                                                           |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                            |
| deepcopy_memo           | 37.0 us                                                | 33.4 us: 1.11x faster                                                           |
| gunicorn                | 1.18 ms                                                | 1.06 ms: 1.11x faster                                                           |
| regex_compile           | 138 ms                                                 | 125 ms: 1.10x faster                                                            |
| aiohttp                 | 1.10 ms                                                | 1000 us: 1.10x faster                                                           |
| pickle_pure_python      | 306 us                                                 | 279 us: 1.10x faster                                                            |
| regex_effbot            | 3.99 ms                                                | 3.65 ms: 1.09x faster                                                           |
| sympy_str               | 290 ms                                                 | 265 ms: 1.09x faster                                                            |
| richards                | 45.7 ms                                                | 41.9 ms: 1.09x faster                                                           |
| fannkuch                | 388 ms                                                 | 356 ms: 1.09x faster                                                            |
| nqueens                 | 83.4 ms                                                | 76.9 ms: 1.08x faster                                                           |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                           |
| spectral_norm           | 100 ms                                                 | 92.7 ms: 1.08x faster                                                           |
| logging_silent          | 101 ns                                                 | 93.8 ns: 1.08x faster                                                           |
| scimark_fft             | 328 ms                                                 | 305 ms: 1.08x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 19.5 ms: 1.08x faster                                                           |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                            |
| chaos                   | 69.2 ms                                                | 64.5 ms: 1.07x faster                                                           |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.20 ms: 1.07x faster                                                           |
| json                    | 4.94 ms                                                | 4.62 ms: 1.07x faster                                                           |
| float                   | 77.2 ms                                                | 72.4 ms: 1.07x faster                                                           |
| mdp                     | 2.62 sec                                               | 2.46 sec: 1.06x faster                                                          |
| hexiom                  | 6.37 ms                                                | 5.99 ms: 1.06x faster                                                           |
| 2to3                    | 259 ms                                                 | 244 ms: 1.06x faster                                                            |
| sympy_expand            | 475 ms                                                 | 449 ms: 1.06x faster                                                            |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                          |
| logging_format          | 6.68 us                                                | 6.33 us: 1.06x faster                                                           |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.05x faster                                                           |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                            |
| deepcopy                | 342 us                                                 | 325 us: 1.05x faster                                                            |
| bench_thread_pool       | 819 us                                                 | 779 us: 1.05x faster                                                            |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                          |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                                           |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.05x faster                                                           |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                            |
| pprint_safe_repr        | 701 ms                                                 | 671 ms: 1.05x faster                                                            |
| pyflate                 | 418 ms                                                 | 401 ms: 1.04x faster                                                            |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                          |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                            |
| scimark_monte_carlo     | 68.1 ms                                                | 65.2 ms: 1.04x faster                                                           |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                                            |
| dulwich_log             | 63.7 ms                                                | 61.2 ms: 1.04x faster                                                           |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                            |
| mako                    | 10.1 ms                                                | 9.76 ms: 1.03x faster                                                           |
| telco                   | 6.58 ms                                                | 6.38 ms: 1.03x faster                                                           |
| tornado_http            | 96.3 ms                                                | 93.3 ms: 1.03x faster                                                           |
| crypto_pyaes            | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                           |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.03x faster                                                            |
| chameleon               | 6.47 ms                                                | 6.33 ms: 1.02x faster                                                           |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                                           |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                            |
| unpack_sequence         | 43.1 ns                                                | 42.4 ns: 1.02x faster                                                           |
| async_tree_none         | 526 ms                                                 | 518 ms: 1.02x faster                                                            |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                                           |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                           |
| coverage                | 100 ms                                                 | 99.2 ms: 1.01x faster                                                           |
| nbody                   | 93.1 ms                                                | 92.4 ms: 1.01x faster                                                           |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                           |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                           |
| regex_dna               | 204 ms                                                 | 205 ms: 1.00x slower                                                            |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.00x slower                                                           |
| async_tree_cpu_io_mixed | 739 ms                                                 | 750 ms: 1.02x slower                                                            |
| django_template         | 32.6 ms                                                | 33.1 ms: 1.02x slower                                                           |
| regex_v8                | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                           |
| xml_etree_process       | 53.9 ms                                                | 55.0 ms: 1.02x slower                                                           |
| pickle                  | 10.1 us                                                | 10.3 us: 1.03x slower                                                           |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                           |
| pickle_list             | 4.11 us                                                | 4.25 us: 1.03x slower                                                           |
| unpickle_list           | 4.91 us                                                | 5.08 us: 1.03x slower                                                           |
| async_tree_memoization  | 627 ms                                                 | 655 ms: 1.04x slower                                                            |
| python_startup          | 8.52 ms                                                | 8.97 ms: 1.05x slower                                                           |
| xml_etree_generate      | 76.2 ms                                                | 80.3 ms: 1.05x slower                                                           |
| python_startup_no_site  | 6.01 ms                                                | 6.52 ms: 1.09x slower                                                           |
| async_generators        | 368 ms                                                 | 422 ms: 1.14x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (6): async_tree_io, pathlib, bench_mp_pool, djangocms, unpickle, thrift
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
