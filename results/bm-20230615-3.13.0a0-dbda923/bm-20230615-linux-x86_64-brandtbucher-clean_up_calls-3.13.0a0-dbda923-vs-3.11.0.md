
# Results vs. 3.11.0

- fork: brandtbucher
- ref: clean_up_calls
- machine: linux-x86_64
- commit hash: dbda923
- commit date: 2023-06-15
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.68 sec: 1.02x slower                                                |
| tornado_http   | 96.3 ms                                                | 98.7 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 90.3 ms: 1.03x faster                                                 |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| float          | 77.2 ms                                                | 80.3 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.39 ms: 1.18x faster                                                 |
| regex_dna      | 204 ms                                                 | 202 ms: 1.01x faster                                                  |
| regex_compile  | 138 ms                                                 | 139 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.93 ms: 1.27x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                                  |
| json_loads           | 26.5 us                                                | 25.3 us: 1.04x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 104 ms: 1.00x slower                                                  |
| pickle_pure_python   | 306 us                                                 | 319 us: 1.04x slower                                                  |
| pickle_dict          | 31.1 us                                                | 33.0 us: 1.06x slower                                                 |
| pickle               | 10.1 us                                                | 10.7 us: 1.07x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                 |
| unpickle             | 13.7 us                                                | 15.1 us: 1.11x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 85.0 ms: 1.12x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.78 us: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (2): tomli_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.18 ms: 1.08x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.67 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 142 us: 3.43x faster                                                  |
| generators               | 73.5 ms                                                | 28.6 ms: 2.57x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.93 ms: 1.27x faster                                                 |
| mypy2                    | 420 ms                                                 | 343 ms: 1.22x faster                                                  |
| regex_effbot             | 3.99 ms                                                | 3.39 ms: 1.18x faster                                                 |
| coroutines               | 25.5 ms                                                | 21.6 ms: 1.18x faster                                                 |
| richards_super           | 56.8 ms                                                | 50.5 ms: 1.12x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.27 ms: 1.12x faster                                                 |
| chaos                    | 69.2 ms                                                | 62.6 ms: 1.11x faster                                                 |
| gc_traversal             | 4.02 ms                                                | 3.68 ms: 1.09x faster                                                 |
| async_tree_none          | 526 ms                                                 | 483 ms: 1.09x faster                                                  |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.08x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 592 ms: 1.06x faster                                                  |
| nqueens                  | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 217 us: 1.05x faster                                                  |
| hexiom                   | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                 |
| json_loads               | 26.5 us                                                | 25.3 us: 1.04x faster                                                 |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.04x faster                                                 |
| coverage                 | 100 ms                                                 | 96.1 ms: 1.04x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                  |
| go                       | 140 ms                                                 | 135 ms: 1.03x faster                                                  |
| nbody                    | 93.1 ms                                                | 90.3 ms: 1.03x faster                                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                                 |
| richards                 | 45.7 ms                                                | 44.7 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 723 ms: 1.02x faster                                                  |
| mdp                      | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                 |
| raytrace                 | 297 ms                                                 | 292 ms: 1.02x faster                                                  |
| logging_silent           | 101 ns                                                 | 99.4 ns: 1.02x faster                                                 |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                |
| regex_dna                | 204 ms                                                 | 202 ms: 1.01x faster                                                  |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                  |
| xml_etree_iterparse      | 104 ms                                                 | 104 ms: 1.00x slower                                                  |
| logging_simple           | 6.03 us                                                | 6.07 us: 1.01x slower                                                 |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                |
| bench_thread_pool        | 819 us                                                 | 826 us: 1.01x slower                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                 |
| regex_compile            | 138 ms                                                 | 139 ms: 1.01x slower                                                  |
| fannkuch                 | 388 ms                                                 | 391 ms: 1.01x slower                                                  |
| sqlglot_optimize         | 53.1 ms                                                | 53.9 ms: 1.02x slower                                                 |
| docutils                 | 2.63 sec                                               | 2.68 sec: 1.02x slower                                                |
| spectral_norm            | 100 ms                                                 | 102 ms: 1.02x slower                                                  |
| tornado_http             | 96.3 ms                                                | 98.7 ms: 1.02x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 720 ms: 1.03x slower                                                  |
| pathlib                  | 18.2 ms                                                | 18.9 ms: 1.04x slower                                                 |
| float                    | 77.2 ms                                                | 80.3 ms: 1.04x slower                                                 |
| pickle_pure_python       | 306 us                                                 | 319 us: 1.04x slower                                                  |
| dulwich_log              | 63.7 ms                                                | 66.8 ms: 1.05x slower                                                 |
| crypto_pyaes             | 74.7 ms                                                | 78.6 ms: 1.05x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 39.1 us: 1.06x slower                                                 |
| telco                    | 6.58 ms                                                | 6.95 ms: 1.06x slower                                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 72.0 ms: 1.06x slower                                                 |
| deepcopy                 | 342 us                                                 | 362 us: 1.06x slower                                                  |
| pickle_dict              | 31.1 us                                                | 33.0 us: 1.06x slower                                                 |
| scimark_fft              | 328 ms                                                 | 348 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.79 ms: 1.06x slower                                                 |
| pickle                   | 10.1 us                                                | 10.7 us: 1.07x slower                                                 |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                 |
| pyflate                  | 418 ms                                                 | 448 ms: 1.07x slower                                                  |
| python_startup           | 8.52 ms                                                | 9.18 ms: 1.08x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.77 us: 1.10x slower                                                 |
| unpickle                 | 13.7 us                                                | 15.1 us: 1.11x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.67 ms: 1.11x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 85.0 ms: 1.12x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.29 us: 1.12x slower                                                 |
| unpack_sequence          | 43.1 ns                                                | 48.9 ns: 1.13x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.78 us: 1.16x slower                                                 |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                                  |
| dask                     | 360 ms                                                 | 527 ms: 1.47x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (7): scimark_sor, regex_v8, tomli_loads, bench_mp_pool, logging_format, scimark_lu, unpickle_list
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
