
# Results vs. base

- fork: gvanrossum
- ref: call_uops_forever
- machine: linux-x86_64
- commit hash: f6a72ae
- commit date: 2023-08-16
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.62 sec                                                              | 2.72 sec: 1.04x slower                                                 |
| tornado_http   | 95.4 ms                                                               | 97.9 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 201 ms: 1.00x slower                                                   |
| float          | 79.1 ms                                                               | 84.8 ms: 1.07x slower                                                  |
| nbody          | 89.9 ms                                                               | 115 ms: 1.28x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                | 214 ms: 1.04x faster                                                   |
| regex_effbot   | 3.69 ms                                                               | 3.74 ms: 1.01x slower                                                  |
| regex_v8       | 23.2 ms                                                               | 24.0 ms: 1.04x slower                                                  |
| regex_compile  | 136 ms                                                                | 155 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_dict          | 33.0 us                                                               | 31.9 us: 1.03x faster                                                  |
| unpickle             | 15.0 us                                                               | 14.6 us: 1.03x faster                                                  |
| json_loads           | 25.4 us                                                               | 25.2 us: 1.01x faster                                                  |
| unpickle_list        | 4.95 us                                                               | 4.99 us: 1.01x slower                                                  |
| pickle_pure_python   | 298 us                                                                | 301 us: 1.01x slower                                                   |
| json_dumps           | 9.77 ms                                                               | 9.87 ms: 1.01x slower                                                  |
| pickle               | 10.6 us                                                               | 10.7 us: 1.01x slower                                                  |
| xml_etree_process    | 57.2 ms                                                               | 58.3 ms: 1.02x slower                                                  |
| xml_etree_generate   | 82.9 ms                                                               | 85.5 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                                | 106 ms: 1.04x slower                                                   |
| unpickle_pure_python | 215 us                                                                | 226 us: 1.05x slower                                                   |
| pickle_list          | 4.62 us                                                               | 4.87 us: 1.05x slower                                                  |
| tomli_loads          | 2.11 sec                                                              | 2.54 sec: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 9.33 ms                                                               | 9.31 ms: 1.00x faster                                                  |
| python_startup_no_site | 6.82 ms                                                               | 6.82 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|-----------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.9 ms                                                               | 12.8 ms: 1.17x slower                                                  |

All benchmarks:
===============

| Benchmark                | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna                | 223 ms                                                                | 214 ms: 1.04x faster                                                   |
| pickle_dict              | 33.0 us                                                               | 31.9 us: 1.03x faster                                                  |
| unpack_sequence          | 48.9 ns                                                               | 47.3 ns: 1.03x faster                                                  |
| unpickle                 | 15.0 us                                                               | 14.6 us: 1.03x faster                                                  |
| coroutines               | 22.0 ms                                                               | 21.7 ms: 1.01x faster                                                  |
| json_loads               | 25.4 us                                                               | 25.2 us: 1.01x faster                                                  |
| python_startup           | 9.33 ms                                                               | 9.31 ms: 1.00x faster                                                  |
| python_startup_no_site   | 6.82 ms                                                               | 6.82 ms: 1.00x faster                                                  |
| pidigits                 | 201 ms                                                                | 201 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                 |
| async_tree_io            | 1.18 sec                                                              | 1.19 sec: 1.00x slower                                                 |
| mdp                      | 2.66 sec                                                              | 2.67 sec: 1.01x slower                                                 |
| generators               | 28.3 ms                                                               | 28.5 ms: 1.01x slower                                                  |
| sqlite_synth             | 2.72 us                                                               | 2.74 us: 1.01x slower                                                  |
| unpickle_list            | 4.95 us                                                               | 4.99 us: 1.01x slower                                                  |
| pickle_pure_python       | 298 us                                                                | 301 us: 1.01x slower                                                   |
| json_dumps               | 9.77 ms                                                               | 9.87 ms: 1.01x slower                                                  |
| deepcopy_reduce          | 3.17 us                                                               | 3.21 us: 1.01x slower                                                  |
| pickle                   | 10.6 us                                                               | 10.7 us: 1.01x slower                                                  |
| scimark_monte_carlo      | 67.2 ms                                                               | 68.2 ms: 1.01x slower                                                  |
| telco                    | 8.00 ms                                                               | 8.12 ms: 1.01x slower                                                  |
| regex_effbot             | 3.69 ms                                                               | 3.74 ms: 1.01x slower                                                  |
| async_tree_memoization   | 562 ms                                                                | 570 ms: 1.01x slower                                                   |
| sqlglot_parse            | 1.30 ms                                                               | 1.32 ms: 1.02x slower                                                  |
| sqlglot_transpile        | 1.62 ms                                                               | 1.64 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed  | 698 ms                                                                | 710 ms: 1.02x slower                                                   |
| xml_etree_process        | 57.2 ms                                                               | 58.3 ms: 1.02x slower                                                  |
| deepcopy                 | 351 us                                                                | 359 us: 1.02x slower                                                   |
| tornado_http             | 95.4 ms                                                               | 97.9 ms: 1.03x slower                                                  |
| dask                     | 518 ms                                                                | 533 ms: 1.03x slower                                                   |
| dulwich_log              | 65.7 ms                                                               | 67.7 ms: 1.03x slower                                                  |
| sqlglot_normalize        | 105 ms                                                                | 109 ms: 1.03x slower                                                   |
| async_generators         | 457 ms                                                                | 472 ms: 1.03x slower                                                   |
| xml_etree_generate       | 82.9 ms                                                               | 85.5 ms: 1.03x slower                                                  |
| async_tree_none          | 435 ms                                                                | 450 ms: 1.03x slower                                                   |
| regex_v8                 | 23.2 ms                                                               | 24.0 ms: 1.04x slower                                                  |
| xml_etree_iterparse      | 102 ms                                                                | 106 ms: 1.04x slower                                                   |
| raytrace                 | 276 ms                                                                | 286 ms: 1.04x slower                                                   |
| pathlib                  | 18.6 ms                                                               | 19.3 ms: 1.04x slower                                                  |
| bench_thread_pool        | 817 us                                                                | 848 us: 1.04x slower                                                   |
| pycparser                | 1.20 sec                                                              | 1.25 sec: 1.04x slower                                                 |
| pprint_safe_repr         | 719 ms                                                                | 747 ms: 1.04x slower                                                   |
| docutils                 | 2.62 sec                                                              | 2.72 sec: 1.04x slower                                                 |
| sqlglot_optimize         | 52.7 ms                                                               | 55.1 ms: 1.04x slower                                                  |
| richards_super           | 54.2 ms                                                               | 56.7 ms: 1.05x slower                                                  |
| pprint_pformat           | 1.47 sec                                                              | 1.54 sec: 1.05x slower                                                 |
| logging_silent           | 100 ns                                                                | 105 ns: 1.05x slower                                                   |
| gc_traversal             | 3.65 ms                                                               | 3.83 ms: 1.05x slower                                                  |
| richards                 | 48.0 ms                                                               | 50.4 ms: 1.05x slower                                                  |
| unpickle_pure_python     | 215 us                                                                | 226 us: 1.05x slower                                                   |
| scimark_sor              | 122 ms                                                                | 129 ms: 1.05x slower                                                   |
| pickle_list              | 4.62 us                                                               | 4.87 us: 1.05x slower                                                  |
| typing_runtime_protocols | 144 us                                                                | 153 us: 1.07x slower                                                   |
| float                    | 79.1 ms                                                               | 84.8 ms: 1.07x slower                                                  |
| go                       | 139 ms                                                                | 150 ms: 1.08x slower                                                   |
| scimark_lu               | 108 ms                                                                | 118 ms: 1.09x slower                                                   |
| crypto_pyaes             | 68.7 ms                                                               | 75.5 ms: 1.10x slower                                                  |
| spectral_norm            | 105 ms                                                                | 116 ms: 1.10x slower                                                   |
| deltablue                | 3.24 ms                                                               | 3.62 ms: 1.12x slower                                                  |
| meteor_contest           | 105 ms                                                                | 118 ms: 1.12x slower                                                   |
| regex_compile            | 136 ms                                                                | 155 ms: 1.14x slower                                                   |
| chaos                    | 60.2 ms                                                               | 69.2 ms: 1.15x slower                                                  |
| deepcopy_memo            | 36.7 us                                                               | 42.5 us: 1.16x slower                                                  |
| pyflate                  | 445 ms                                                                | 519 ms: 1.17x slower                                                   |
| mako                     | 10.9 ms                                                               | 12.8 ms: 1.17x slower                                                  |
| tomli_loads              | 2.11 sec                                                              | 2.54 sec: 1.21x slower                                                 |
| scimark_fft              | 350 ms                                                                | 425 ms: 1.21x slower                                                   |
| nqueens                  | 81.4 ms                                                               | 99.4 ms: 1.22x slower                                                  |
| fannkuch                 | 388 ms                                                                | 480 ms: 1.24x slower                                                   |
| comprehensions           | 20.6 us                                                               | 26.0 us: 1.26x slower                                                  |
| nbody                    | 89.9 ms                                                               | 115 ms: 1.28x slower                                                   |
| hexiom                   | 5.99 ms                                                               | 8.00 ms: 1.34x slower                                                  |
| scimark_sparse_mat_mult  | 4.51 ms                                                               | 6.19 ms: 1.37x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.05x slower                                                           |

Benchmark hidden because not significant (9): logging_simple, logging_format, xml_etree_parse, coverage, asyncio_tcp, bench_mp_pool, create_gc_cycles, json, mypy2


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x
