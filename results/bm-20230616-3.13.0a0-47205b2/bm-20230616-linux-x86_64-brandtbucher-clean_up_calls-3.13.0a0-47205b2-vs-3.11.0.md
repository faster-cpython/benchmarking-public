
# Results vs. 3.11.0

- fork: brandtbucher
- ref: clean_up_calls
- machine: linux-x86_64
- commit hash: 47205b2
- commit date: 2023-06-16
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                |
| tornado_http   | 96.3 ms                                                | 96.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 91.3 ms: 1.02x faster                                                 |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| float          | 77.2 ms                                                | 81.2 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                  |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                  |
| regex_effbot   | 3.99 ms                                                | 4.09 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.86 ms: 1.28x faster                                                 |
| json_loads           | 26.5 us                                                | 24.9 us: 1.06x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.05x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                                  |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                                 |
| pickle_pure_python   | 306 us                                                 | 316 us: 1.03x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.09 us: 1.04x slower                                                 |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.3 ms: 1.11x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.61 us: 1.12x slower                                                 |
| unpickle             | 13.7 us                                                | 15.3 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.16 ms: 1.07x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.65 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 141 us: 3.45x faster                                                  |
| generators               | 73.5 ms                                                | 29.0 ms: 2.53x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 507 ms: 1.82x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.86 ms: 1.28x faster                                                 |
| mypy2                    | 420 ms                                                 | 339 ms: 1.24x faster                                                  |
| deltablue                | 3.67 ms                                                | 3.29 ms: 1.12x faster                                                 |
| chaos                    | 69.2 ms                                                | 62.0 ms: 1.12x faster                                                 |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                                 |
| richards_super           | 56.8 ms                                                | 51.8 ms: 1.09x faster                                                 |
| gc_traversal             | 4.02 ms                                                | 3.69 ms: 1.09x faster                                                 |
| async_tree_none          | 526 ms                                                 | 482 ms: 1.09x faster                                                  |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.32 ms: 1.06x faster                                                 |
| coroutines               | 25.5 ms                                                | 24.0 ms: 1.06x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 590 ms: 1.06x faster                                                  |
| json_loads               | 26.5 us                                                | 24.9 us: 1.06x faster                                                 |
| hexiom                   | 6.37 ms                                                | 6.04 ms: 1.06x faster                                                 |
| nqueens                  | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                 |
| coverage                 | 100 ms                                                 | 95.5 ms: 1.05x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 218 us: 1.05x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.03x faster                                                  |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 720 ms: 1.03x faster                                                  |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                  |
| nbody                    | 93.1 ms                                                | 91.3 ms: 1.02x faster                                                 |
| logging_format           | 6.68 us                                                | 6.56 us: 1.02x faster                                                 |
| mdp                      | 2.62 sec                                               | 2.57 sec: 1.02x faster                                                |
| richards                 | 45.7 ms                                                | 45.0 ms: 1.02x faster                                                 |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                                 |
| bench_thread_pool        | 819 us                                                 | 822 us: 1.00x slower                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.49 ms: 1.00x slower                                                 |
| logging_simple           | 6.03 us                                                | 6.06 us: 1.00x slower                                                 |
| tornado_http             | 96.3 ms                                                | 96.8 ms: 1.01x slower                                                 |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                |
| fannkuch                 | 388 ms                                                 | 393 ms: 1.01x slower                                                  |
| regex_dna                | 204 ms                                                 | 207 ms: 1.02x slower                                                  |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                |
| pathlib                  | 18.2 ms                                                | 18.6 ms: 1.02x slower                                                 |
| pickle_dict              | 31.1 us                                                | 31.8 us: 1.02x slower                                                 |
| regex_effbot             | 3.99 ms                                                | 4.09 ms: 1.02x slower                                                 |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.03x slower                                                  |
| dulwich_log              | 63.7 ms                                                | 65.5 ms: 1.03x slower                                                 |
| pickle_pure_python       | 306 us                                                 | 316 us: 1.03x slower                                                  |
| deepcopy_memo            | 37.0 us                                                | 38.3 us: 1.03x slower                                                 |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                                  |
| unpickle_list            | 4.91 us                                                | 5.09 us: 1.04x slower                                                 |
| crypto_pyaes             | 74.7 ms                                                | 77.6 ms: 1.04x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 730 ms: 1.04x slower                                                  |
| telco                    | 6.58 ms                                                | 6.87 ms: 1.04x slower                                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 71.4 ms: 1.05x slower                                                 |
| float                    | 77.2 ms                                                | 81.2 ms: 1.05x slower                                                 |
| deepcopy                 | 342 us                                                 | 363 us: 1.06x slower                                                  |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                                 |
| pyflate                  | 418 ms                                                 | 447 ms: 1.07x slower                                                  |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.16 ms: 1.07x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                                 |
| scimark_fft              | 328 ms                                                 | 360 ms: 1.10x slower                                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.25 us: 1.10x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 84.3 ms: 1.11x slower                                                 |
| unpack_sequence          | 43.1 ns                                                | 47.7 ns: 1.11x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.65 ms: 1.11x slower                                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.01 ms: 1.11x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.61 us: 1.12x slower                                                 |
| unpickle                 | 13.7 us                                                | 15.3 us: 1.12x slower                                                 |
| async_generators         | 368 ms                                                 | 459 ms: 1.25x slower                                                  |
| dask                     | 360 ms                                                 | 526 ms: 1.46x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (7): meteor_contest, xml_etree_iterparse, tomli_loads, logging_silent, bench_mp_pool, raytrace, regex_v8
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
