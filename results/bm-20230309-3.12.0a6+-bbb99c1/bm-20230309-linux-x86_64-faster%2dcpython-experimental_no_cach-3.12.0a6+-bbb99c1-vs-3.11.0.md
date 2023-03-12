
# Results vs. 3.11.0

- fork: faster-cpython
- ref: experimental_no_cach
- machine: linux-x86_64
- commit hash: bbb99c1
- commit date: 2023-03-09
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                             |
| chameleon      | 6.38 ms                                                | 6.54 ms: 1.02x slower                                                            |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                           |
| html5lib       | 64.8 ms                                                | 61.0 ms: 1.06x faster                                                            |
| tornado_http   | 96.5 ms                                                | 95.1 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                             |
| float          | 76.8 ms                                                | 73.8 ms: 1.04x faster                                                            |
| nbody          | 90.0 ms                                                | 95.1 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 133 ms: 1.03x faster                                                             |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                            |
| regex_effbot   | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                            |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                                            |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                             |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                             |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                            |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                                             |
| pickle_list          | 4.14 us                                                | 4.04 us: 1.03x faster                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| pickle_dict          | 31.2 us                                                | 31.5 us: 1.01x slower                                                            |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                            |
| xml_etree_process    | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                            |
| unpickle             | 13.3 us                                                | 14.0 us: 1.05x slower                                                            |
| xml_etree_generate   | 75.9 ms                                                | 80.7 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                            |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.6 ms: 1.06x faster                                                            |
| mako            | 9.83 ms                                                | 9.86 ms: 1.00x slower                                                            |
| genshi_text     | 21.5 ms                                                | 22.1 ms: 1.03x slower                                                            |
| django_template | 32.3 ms                                                | 33.8 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.8 ms: 2.47x faster                                                            |
| asyncio_tcp             | 883 ms                                                 | 509 ms: 1.74x faster                                                             |
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                                            |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                             |
| coroutines              | 26.2 ms                                                | 22.8 ms: 1.15x faster                                                            |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                             |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.13x faster                                                            |
| mdp                     | 2.63 sec                                               | 2.42 sec: 1.09x faster                                                           |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                             |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                            |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                                             |
| richards                | 46.1 ms                                                | 43.0 ms: 1.07x faster                                                            |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                                             |
| html5lib                | 64.8 ms                                                | 61.0 ms: 1.06x faster                                                            |
| genshi_xml              | 51.4 ms                                                | 48.6 ms: 1.06x faster                                                            |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                            |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                                            |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                                             |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                           |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                             |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                                            |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                            |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                             |
| float                   | 76.8 ms                                                | 73.8 ms: 1.04x faster                                                            |
| unpack_sequence         | 44.5 ns                                                | 42.8 ns: 1.04x faster                                                            |
| pprint_safe_repr        | 706 ms                                                 | 680 ms: 1.04x faster                                                             |
| logging_simple          | 6.02 us                                                | 5.81 us: 1.04x faster                                                            |
| bench_thread_pool       | 817 us                                                 | 789 us: 1.03x faster                                                             |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                             |
| nqueens                 | 83.8 ms                                                | 81.0 ms: 1.03x faster                                                            |
| coverage                | 99.3 ms                                                | 96.0 ms: 1.03x faster                                                            |
| logging_format          | 6.48 us                                                | 6.27 us: 1.03x faster                                                            |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                           |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                             |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                             |
| hexiom                  | 6.34 ms                                                | 6.16 ms: 1.03x faster                                                            |
| scimark_fft             | 325 ms                                                 | 317 ms: 1.03x faster                                                             |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                            |
| pickle_list             | 4.14 us                                                | 4.04 us: 1.03x faster                                                            |
| deepcopy                | 341 us                                                 | 333 us: 1.03x faster                                                             |
| regex_compile           | 136 ms                                                 | 133 ms: 1.03x faster                                                             |
| sympy_str               | 291 ms                                                 | 284 ms: 1.03x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                            |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                           |
| pyflate                 | 419 ms                                                 | 410 ms: 1.02x faster                                                             |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                            |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.02x faster                                                            |
| crypto_pyaes            | 75.7 ms                                                | 74.3 ms: 1.02x faster                                                            |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.50 ms: 1.02x faster                                                            |
| chaos                   | 68.7 ms                                                | 67.5 ms: 1.02x faster                                                            |
| tornado_http            | 96.5 ms                                                | 95.1 ms: 1.02x faster                                                            |
| gc_traversal            | 3.82 ms                                                | 3.77 ms: 1.01x faster                                                            |
| scimark_monte_carlo     | 68.0 ms                                                | 67.1 ms: 1.01x faster                                                            |
| spectral_norm           | 98.1 ms                                                | 96.9 ms: 1.01x faster                                                            |
| deepcopy_reduce         | 3.02 us                                                | 2.99 us: 1.01x faster                                                            |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                           |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                             |
| regex_effbot            | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                            |
| mako                    | 9.83 ms                                                | 9.86 ms: 1.00x slower                                                            |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                                             |
| sympy_sum               | 166 ms                                                 | 167 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                 | 744 ms: 1.01x slower                                                             |
| pickle_dict             | 31.2 us                                                | 31.5 us: 1.01x slower                                                            |
| chameleon               | 6.38 ms                                                | 6.54 ms: 1.02x slower                                                            |
| telco                   | 6.43 ms                                                | 6.59 ms: 1.03x slower                                                            |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                            |
| thrift                  | 760 us                                                 | 780 us: 1.03x slower                                                             |
| genshi_text             | 21.5 ms                                                | 22.1 ms: 1.03x slower                                                            |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                             |
| xml_etree_process       | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                            |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                            |
| django_template         | 32.3 ms                                                | 33.8 ms: 1.05x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                            |
| python_startup          | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                            |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                            |
| async_tree_memoization  | 624 ms                                                 | 657 ms: 1.05x slower                                                             |
| unpickle                | 13.3 us                                                | 14.0 us: 1.05x slower                                                            |
| nbody                   | 90.0 ms                                                | 95.1 ms: 1.06x slower                                                            |
| xml_etree_generate      | 75.9 ms                                                | 80.7 ms: 1.06x slower                                                            |
| python_startup_no_site  | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                            |
| async_generators        | 356 ms                                                 | 411 ms: 1.16x slower                                                             |
| dask                    | 365 ms                                                 | 509 ms: 1.39x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (8): sqlalchemy_declarative, dulwich_log, unpickle_list, async_tree_none, bench_mp_pool, djangocms, sqlalchemy_imperative, logging_silent
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230309-3.12.0a6+-bbb99c1/bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1.json: comprehensions
