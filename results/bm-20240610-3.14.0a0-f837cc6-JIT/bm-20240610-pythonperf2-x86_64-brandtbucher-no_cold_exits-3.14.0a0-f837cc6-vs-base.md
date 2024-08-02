# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.00x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                                      | 304 ms: 1.00x faster                                                       |
| docutils       | 3.11 sec                                                                    | 3.09 sec: 1.00x faster                                                     |
| html5lib       | 73.0 ms                                                                     | 73.3 ms: 1.01x slower                                                      |
| tornado_http   | 123 ms                                                                      | 122 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 629 ms                                                                      | 620 ms: 1.02x faster                                                       |
| Geometric mean          | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                                      | 250 ms: 1.00x faster                                                       |
| float          | 73.2 ms                                                                     | 75.5 ms: 1.03x slower                                                      |
| nbody          | 81.1 ms                                                                     | 84.1 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                      | 136 ms: 1.01x faster                                                       |
| regex_effbot   | 3.54 ms                                                                     | 3.49 ms: 1.01x faster                                                      |
| regex_dna      | 240 ms                                                                      | 239 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 33.3 us                                                                     | 31.1 us: 1.07x faster                                                      |
| pickle               | 10.8 us                                                                     | 10.5 us: 1.03x faster                                                      |
| pickle_list          | 4.59 us                                                                     | 4.48 us: 1.02x faster                                                      |
| pickle_pure_python   | 318 us                                                                      | 315 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 99.8 ms                                                                     | 99.0 ms: 1.01x faster                                                      |
| xml_etree_parse      | 144 ms                                                                      | 143 ms: 1.01x faster                                                       |
| unpickle_list        | 4.96 us                                                                     | 4.93 us: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                                      | 217 us: 1.01x slower                                                       |
| xml_etree_process    | 58.1 ms                                                                     | 58.6 ms: 1.01x slower                                                      |
| xml_etree_generate   | 81.1 ms                                                                     | 81.8 ms: 1.01x slower                                                      |
| unpickle             | 15.5 us                                                                     | 16.0 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (3): json_loads, tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.46 ms                                                                     | 8.86 ms: 1.07x faster                                                      |
| python_startup         | 13.8 ms                                                                     | 13.2 ms: 1.05x faster                                                      |
| Geometric mean         | (ref)                                                                       | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 29.5 ms                                                                     | 28.1 ms: 1.05x faster                                                      |
| genshi_xml      | 66.8 ms                                                                     | 64.9 ms: 1.03x faster                                                      |
| django_template | 41.8 ms                                                                     | 41.0 ms: 1.02x faster                                                      |
| mako            | 9.19 ms                                                                     | 9.15 ms: 1.00x faster                                                      |
| Geometric mean  | (ref)                                                                       | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict              | 33.3 us                                                                     | 31.1 us: 1.07x faster                                                      |
| python_startup_no_site   | 9.46 ms                                                                     | 8.86 ms: 1.07x faster                                                      |
| nqueens                  | 99.7 ms                                                                     | 94.9 ms: 1.05x faster                                                      |
| logging_silent           | 107 ns                                                                      | 102 ns: 1.05x faster                                                       |
| genshi_text              | 29.5 ms                                                                     | 28.1 ms: 1.05x faster                                                      |
| python_startup           | 13.8 ms                                                                     | 13.2 ms: 1.05x faster                                                      |
| spectral_norm            | 86.5 ms                                                                     | 83.0 ms: 1.04x faster                                                      |
| pyflate                  | 469 ms                                                                      | 453 ms: 1.03x faster                                                       |
| bench_mp_pool            | 4.93 ms                                                                     | 4.77 ms: 1.03x faster                                                      |
| logging_simple           | 6.58 us                                                                     | 6.39 us: 1.03x faster                                                      |
| genshi_xml               | 66.8 ms                                                                     | 64.9 ms: 1.03x faster                                                      |
| pickle                   | 10.8 us                                                                     | 10.5 us: 1.03x faster                                                      |
| deepcopy_memo            | 37.5 us                                                                     | 36.5 us: 1.03x faster                                                      |
| pickle_list              | 4.59 us                                                                     | 4.48 us: 1.02x faster                                                      |
| pprint_pformat           | 1.65 sec                                                                    | 1.61 sec: 1.02x faster                                                     |
| fannkuch                 | 344 ms                                                                      | 336 ms: 1.02x faster                                                       |
| raytrace                 | 292 ms                                                                      | 286 ms: 1.02x faster                                                       |
| async_generators         | 399 ms                                                                      | 391 ms: 1.02x faster                                                       |
| richards                 | 44.2 ms                                                                     | 43.2 ms: 1.02x faster                                                      |
| logging_format           | 7.16 us                                                                     | 7.02 us: 1.02x faster                                                      |
| django_template          | 41.8 ms                                                                     | 41.0 ms: 1.02x faster                                                      |
| chaos                    | 66.8 ms                                                                     | 65.7 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed  | 629 ms                                                                      | 620 ms: 1.02x faster                                                       |
| pprint_safe_repr         | 799 ms                                                                      | 787 ms: 1.02x faster                                                       |
| regex_compile            | 137 ms                                                                      | 136 ms: 1.01x faster                                                       |
| regex_effbot             | 3.54 ms                                                                     | 3.49 ms: 1.01x faster                                                      |
| sympy_sum                | 166 ms                                                                      | 164 ms: 1.01x faster                                                       |
| sympy_expand             | 531 ms                                                                      | 525 ms: 1.01x faster                                                       |
| hexiom                   | 6.76 ms                                                                     | 6.68 ms: 1.01x faster                                                      |
| pickle_pure_python       | 318 us                                                                      | 315 us: 1.01x faster                                                       |
| tornado_http             | 123 ms                                                                      | 122 ms: 1.01x faster                                                       |
| richards_super           | 51.8 ms                                                                     | 51.3 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 99.8 ms                                                                     | 99.0 ms: 1.01x faster                                                      |
| xml_etree_parse          | 144 ms                                                                      | 143 ms: 1.01x faster                                                       |
| sympy_integrate          | 25.6 ms                                                                     | 25.4 ms: 1.01x faster                                                      |
| deepcopy                 | 411 us                                                                      | 408 us: 1.01x faster                                                       |
| comprehensions           | 18.2 us                                                                     | 18.1 us: 1.01x faster                                                      |
| sqlglot_transpile        | 1.83 ms                                                                     | 1.82 ms: 1.01x faster                                                      |
| sqlite_synth             | 2.79 us                                                                     | 2.77 us: 1.01x faster                                                      |
| meteor_contest           | 129 ms                                                                      | 128 ms: 1.01x faster                                                       |
| unpickle_list            | 4.96 us                                                                     | 4.93 us: 1.01x faster                                                      |
| sqlglot_parse            | 1.42 ms                                                                     | 1.42 ms: 1.01x faster                                                      |
| sympy_str                | 312 ms                                                                      | 310 ms: 1.01x faster                                                       |
| regex_dna                | 240 ms                                                                      | 239 ms: 1.01x faster                                                       |
| 2to3                     | 305 ms                                                                      | 304 ms: 1.00x faster                                                       |
| telco                    | 8.27 ms                                                                     | 8.23 ms: 1.00x faster                                                      |
| docutils                 | 3.11 sec                                                                    | 3.09 sec: 1.00x faster                                                     |
| mako                     | 9.19 ms                                                                     | 9.15 ms: 1.00x faster                                                      |
| pidigits                 | 251 ms                                                                      | 250 ms: 1.00x faster                                                       |
| mdp                      | 2.55 sec                                                                    | 2.56 sec: 1.00x slower                                                     |
| html5lib                 | 73.0 ms                                                                     | 73.3 ms: 1.01x slower                                                      |
| unpickle_pure_python     | 216 us                                                                      | 217 us: 1.01x slower                                                       |
| xml_etree_process        | 58.1 ms                                                                     | 58.6 ms: 1.01x slower                                                      |
| xml_etree_generate       | 81.1 ms                                                                     | 81.8 ms: 1.01x slower                                                      |
| crypto_pyaes             | 69.9 ms                                                                     | 70.5 ms: 1.01x slower                                                      |
| coverage                 | 78.8 ms                                                                     | 79.6 ms: 1.01x slower                                                      |
| pathlib                  | 16.0 ms                                                                     | 16.2 ms: 1.01x slower                                                      |
| sqlglot_optimize         | 63.3 ms                                                                     | 64.0 ms: 1.01x slower                                                      |
| generators               | 34.3 ms                                                                     | 34.8 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 184 us                                                                      | 187 us: 1.01x slower                                                       |
| bench_thread_pool        | 951 us                                                                      | 965 us: 1.02x slower                                                       |
| coroutines               | 21.5 ms                                                                     | 21.9 ms: 1.02x slower                                                      |
| sqlglot_normalize        | 127 ms                                                                      | 130 ms: 1.02x slower                                                       |
| scimark_monte_carlo      | 65.7 ms                                                                     | 67.3 ms: 1.02x slower                                                      |
| unpickle                 | 15.5 us                                                                     | 16.0 us: 1.03x slower                                                      |
| float                    | 73.2 ms                                                                     | 75.5 ms: 1.03x slower                                                      |
| scimark_fft              | 284 ms                                                                      | 293 ms: 1.03x slower                                                       |
| scimark_lu               | 113 ms                                                                      | 117 ms: 1.03x slower                                                       |
| nbody                    | 81.1 ms                                                                     | 84.1 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 3.95 ms                                                                     | 4.13 ms: 1.04x slower                                                      |
| scimark_sor              | 130 ms                                                                      | 137 ms: 1.05x slower                                                       |
| gc_traversal             | 4.38 ms                                                                     | 4.88 ms: 1.12x slower                                                      |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (24): async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_none, dask, async_tree_io, pylint, async_tree_io_tg, thrift, deltablue, asyncio_tcp, json_loads, tomli_loads, dulwich_log, json_dumps, asyncio_tcp_ssl, asyncio_websockets, pycparser, create_gc_cycles, go, json, deepcopy_reduce, regex_v8

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x