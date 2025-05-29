# Results vs. base

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.025x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                                                                | 279 ms: 1.01x faster                                                                                                        |
| docutils       | 2.87 sec                                                                                                              | 2.89 sec: 1.01x slower                                                                                                      |
| html5lib       | 66.3 ms                                                                                                               | 65.6 ms: 1.01x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                 | 1.00x faster                                                                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|-------------------------|:---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| coroutines              | 22.1 ms                                                                                                               | 20.9 ms: 1.06x faster                                                                                                       |
| async_tree_none         | 286 ms                                                                                                                | 272 ms: 1.05x faster                                                                                                        |
| async_tree_memoization  | 329 ms                                                                                                                | 313 ms: 1.05x faster                                                                                                        |
| async_tree_io           | 629 ms                                                                                                                | 604 ms: 1.04x faster                                                                                                        |
| asyncio_tcp             | 373 ms                                                                                                                | 371 ms: 1.01x faster                                                                                                        |
| asyncio_tcp_ssl         | 1.59 sec                                                                                                              | 1.58 sec: 1.00x faster                                                                                                      |
| async_tree_cpu_io_mixed | 503 ms                                                                                                                | 518 ms: 1.03x slower                                                                                                        |
| async_generators        | 429 ms                                                                                                                | 447 ms: 1.04x slower                                                                                                        |
| Geometric mean          | (ref)                                                                                                                 | 1.02x faster                                                                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| float          | 70.1 ms                                                                                                               | 65.8 ms: 1.07x faster                                                                                                       |
| pidigits       | 257 ms                                                                                                                | 292 ms: 1.14x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                 | 1.02x slower                                                                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                                                                | 131 ms: 1.02x faster                                                                                                        |
| regex_dna      | 240 ms                                                                                                                | 242 ms: 1.01x slower                                                                                                        |
| regex_effbot   | 3.43 ms                                                                                                               | 3.52 ms: 1.03x slower                                                                                                       |
| regex_v8       | 24.6 ms                                                                                                               | 28.3 ms: 1.15x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                 | 1.04x slower                                                                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| pickle_list          | 4.96 us                                                                                                               | 4.48 us: 1.11x faster                                                                                                       |
| pickle_dict          | 34.6 us                                                                                                               | 31.3 us: 1.11x faster                                                                                                       |
| unpickle_pure_python | 215 us                                                                                                                | 202 us: 1.07x faster                                                                                                        |
| xml_etree_generate   | 85.0 ms                                                                                                               | 80.0 ms: 1.06x faster                                                                                                       |
| pickle_pure_python   | 330 us                                                                                                                | 313 us: 1.06x faster                                                                                                        |
| unpickle             | 14.4 us                                                                                                               | 13.7 us: 1.05x faster                                                                                                       |
| xml_etree_process    | 58.8 ms                                                                                                               | 56.3 ms: 1.04x faster                                                                                                       |
| tomli_loads          | 2.09 sec                                                                                                              | 2.01 sec: 1.04x faster                                                                                                      |
| pickle               | 12.2 us                                                                                                               | 12.0 us: 1.02x faster                                                                                                       |
| json_dumps           | 11.9 ms                                                                                                               | 12.0 ms: 1.01x slower                                                                                                       |
| xml_etree_iterparse  | 98.2 ms                                                                                                               | 103 ms: 1.05x slower                                                                                                        |
| xml_etree_parse      | 141 ms                                                                                                                | 167 ms: 1.18x slower                                                                                                        |
| Geometric mean       | (ref)                                                                                                                 | 1.02x faster                                                                                                                |

Benchmark hidden because not significant (2): json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.6 ms                                                                                                               | 13.7 ms: 1.00x slower                                                                                                       |
| python_startup_no_site | 8.77 ms                                                                                                               | 8.90 ms: 1.01x slower                                                                                                       |
| Geometric mean         | (ref)                                                                                                                 | 1.01x slower                                                                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 23.3 ms                                                                                                               | 22.1 ms: 1.05x faster                                                                                                       |
| django_template | 35.8 ms                                                                                                               | 34.4 ms: 1.04x faster                                                                                                       |
| genshi_xml      | 53.3 ms                                                                                                               | 52.2 ms: 1.02x faster                                                                                                       |
| mako            | 10.8 ms                                                                                                               | 11.1 ms: 1.02x slower                                                                                                       |
| Geometric mean  | (ref)                                                                                                                 | 1.02x faster                                                                                                                |

All benchmarks:
===============

| Benchmark                | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| gc_traversal             | 6.42 ms                                                                                                               | 5.42 ms: 1.18x faster                                                                                                       |
| scimark_sor              | 105 ms                                                                                                                | 91.5 ms: 1.15x faster                                                                                                       |
| scimark_fft              | 313 ms                                                                                                                | 279 ms: 1.12x faster                                                                                                        |
| raytrace                 | 282 ms                                                                                                                | 253 ms: 1.12x faster                                                                                                        |
| pyflate                  | 452 ms                                                                                                                | 405 ms: 1.12x faster                                                                                                        |
| pickle_list              | 4.96 us                                                                                                               | 4.48 us: 1.11x faster                                                                                                       |
| pickle_dict              | 34.6 us                                                                                                               | 31.3 us: 1.11x faster                                                                                                       |
| scimark_sparse_mat_mult  | 4.75 ms                                                                                                               | 4.30 ms: 1.10x faster                                                                                                       |
| deepcopy_reduce          | 2.96 us                                                                                                               | 2.70 us: 1.10x faster                                                                                                       |
| coverage                 | 84.6 ms                                                                                                               | 77.6 ms: 1.09x faster                                                                                                       |
| deepcopy                 | 278 us                                                                                                                | 257 us: 1.08x faster                                                                                                        |
| hexiom                   | 6.08 ms                                                                                                               | 5.62 ms: 1.08x faster                                                                                                       |
| telco                    | 7.91 ms                                                                                                               | 7.30 ms: 1.08x faster                                                                                                       |
| scimark_lu               | 95.2 ms                                                                                                               | 88.1 ms: 1.08x faster                                                                                                       |
| spectral_norm            | 92.6 ms                                                                                                               | 86.0 ms: 1.08x faster                                                                                                       |
| float                    | 70.1 ms                                                                                                               | 65.8 ms: 1.07x faster                                                                                                       |
| unpickle_pure_python     | 215 us                                                                                                                | 202 us: 1.07x faster                                                                                                        |
| richards                 | 44.9 ms                                                                                                               | 42.3 ms: 1.06x faster                                                                                                       |
| xml_etree_generate       | 85.0 ms                                                                                                               | 80.0 ms: 1.06x faster                                                                                                       |
| coroutines               | 22.1 ms                                                                                                               | 20.9 ms: 1.06x faster                                                                                                       |
| pickle_pure_python       | 330 us                                                                                                                | 313 us: 1.06x faster                                                                                                        |
| chaos                    | 60.0 ms                                                                                                               | 56.9 ms: 1.05x faster                                                                                                       |
| richards_super           | 51.1 ms                                                                                                               | 48.5 ms: 1.05x faster                                                                                                       |
| genshi_text              | 23.3 ms                                                                                                               | 22.1 ms: 1.05x faster                                                                                                       |
| async_tree_none          | 286 ms                                                                                                                | 272 ms: 1.05x faster                                                                                                        |
| async_tree_memoization   | 329 ms                                                                                                                | 313 ms: 1.05x faster                                                                                                        |
| thrift                   | 851 us                                                                                                                | 809 us: 1.05x faster                                                                                                        |
| deepcopy_memo            | 27.6 us                                                                                                               | 26.2 us: 1.05x faster                                                                                                       |
| bench_thread_pool        | 986 us                                                                                                                | 940 us: 1.05x faster                                                                                                        |
| unpickle                 | 14.4 us                                                                                                               | 13.7 us: 1.05x faster                                                                                                       |
| pathlib                  | 17.4 ms                                                                                                               | 16.6 ms: 1.05x faster                                                                                                       |
| crypto_pyaes             | 79.8 ms                                                                                                               | 76.3 ms: 1.05x faster                                                                                                       |
| typing_runtime_protocols | 171 us                                                                                                                | 164 us: 1.05x faster                                                                                                        |
| xml_etree_process        | 58.8 ms                                                                                                               | 56.3 ms: 1.04x faster                                                                                                       |
| scimark_monte_carlo      | 60.0 ms                                                                                                               | 57.5 ms: 1.04x faster                                                                                                       |
| async_tree_io            | 629 ms                                                                                                                | 604 ms: 1.04x faster                                                                                                        |
| django_template          | 35.8 ms                                                                                                               | 34.4 ms: 1.04x faster                                                                                                       |
| tomli_loads              | 2.09 sec                                                                                                              | 2.01 sec: 1.04x faster                                                                                                      |
| comprehensions           | 17.1 us                                                                                                               | 16.5 us: 1.04x faster                                                                                                       |
| sqlglot_v2_parse         | 1.32 ms                                                                                                               | 1.27 ms: 1.03x faster                                                                                                       |
| sqlglot_v2_transpile     | 1.70 ms                                                                                                               | 1.65 ms: 1.03x faster                                                                                                       |
| go                       | 125 ms                                                                                                                | 121 ms: 1.03x faster                                                                                                        |
| nqueens                  | 92.2 ms                                                                                                               | 89.4 ms: 1.03x faster                                                                                                       |
| sqlite_synth             | 2.89 us                                                                                                               | 2.80 us: 1.03x faster                                                                                                       |
| pprint_safe_repr         | 782 ms                                                                                                                | 758 ms: 1.03x faster                                                                                                        |
| pprint_pformat           | 1.59 sec                                                                                                              | 1.54 sec: 1.03x faster                                                                                                      |
| logging_silent           | 517 ns                                                                                                                | 504 ns: 1.02x faster                                                                                                        |
| sqlglot_v2_optimize      | 56.7 ms                                                                                                               | 55.3 ms: 1.02x faster                                                                                                       |
| deltablue                | 3.13 ms                                                                                                               | 3.05 ms: 1.02x faster                                                                                                       |
| sympy_expand             | 497 ms                                                                                                                | 485 ms: 1.02x faster                                                                                                        |
| logging_simple           | 6.59 us                                                                                                               | 6.45 us: 1.02x faster                                                                                                       |
| genshi_xml               | 53.3 ms                                                                                                               | 52.2 ms: 1.02x faster                                                                                                       |
| regex_compile            | 134 ms                                                                                                                | 131 ms: 1.02x faster                                                                                                        |
| dulwich_log              | 60.0 ms                                                                                                               | 58.9 ms: 1.02x faster                                                                                                       |
| pylint                   | 324 ms                                                                                                                | 317 ms: 1.02x faster                                                                                                        |
| sympy_sum                | 152 ms                                                                                                                | 149 ms: 1.02x faster                                                                                                        |
| sqlglot_v2_normalize     | 114 ms                                                                                                                | 112 ms: 1.02x faster                                                                                                        |
| bpe_tokeniser            | 4.68 sec                                                                                                              | 4.60 sec: 1.02x faster                                                                                                      |
| pickle                   | 12.2 us                                                                                                               | 12.0 us: 1.02x faster                                                                                                       |
| many_optionals           | 1.02 ms                                                                                                               | 1.00 ms: 1.02x faster                                                                                                       |
| sympy_str                | 289 ms                                                                                                                | 285 ms: 1.01x faster                                                                                                        |
| sympy_integrate          | 22.1 ms                                                                                                               | 21.8 ms: 1.01x faster                                                                                                       |
| mdp                      | 1.29 sec                                                                                                              | 1.27 sec: 1.01x faster                                                                                                      |
| json                     | 5.39 ms                                                                                                               | 5.32 ms: 1.01x faster                                                                                                       |
| html5lib                 | 66.3 ms                                                                                                               | 65.6 ms: 1.01x faster                                                                                                       |
| 2to3                     | 281 ms                                                                                                                | 279 ms: 1.01x faster                                                                                                        |
| subparsers               | 24.3 ms                                                                                                               | 24.1 ms: 1.01x faster                                                                                                       |
| asyncio_tcp              | 373 ms                                                                                                                | 371 ms: 1.01x faster                                                                                                        |
| asyncio_tcp_ssl          | 1.59 sec                                                                                                              | 1.58 sec: 1.00x faster                                                                                                      |
| python_startup           | 13.6 ms                                                                                                               | 13.7 ms: 1.00x slower                                                                                                       |
| regex_dna                | 240 ms                                                                                                                | 242 ms: 1.01x slower                                                                                                        |
| docutils                 | 2.87 sec                                                                                                              | 2.89 sec: 1.01x slower                                                                                                      |
| logging_format           | 7.13 us                                                                                                               | 7.19 us: 1.01x slower                                                                                                       |
| json_dumps               | 11.9 ms                                                                                                               | 12.0 ms: 1.01x slower                                                                                                       |
| python_startup_no_site   | 8.77 ms                                                                                                               | 8.90 ms: 1.01x slower                                                                                                       |
| mako                     | 10.8 ms                                                                                                               | 11.1 ms: 1.02x slower                                                                                                       |
| regex_effbot             | 3.43 ms                                                                                                               | 3.52 ms: 1.03x slower                                                                                                       |
| fannkuch                 | 369 ms                                                                                                                | 379 ms: 1.03x slower                                                                                                        |
| async_tree_cpu_io_mixed  | 503 ms                                                                                                                | 518 ms: 1.03x slower                                                                                                        |
| create_gc_cycles         | 2.80 ms                                                                                                               | 2.90 ms: 1.03x slower                                                                                                       |
| async_generators         | 429 ms                                                                                                                | 447 ms: 1.04x slower                                                                                                        |
| xml_etree_iterparse      | 98.2 ms                                                                                                               | 103 ms: 1.05x slower                                                                                                        |
| meteor_contest           | 128 ms                                                                                                                | 135 ms: 1.06x slower                                                                                                        |
| generators               | 28.3 ms                                                                                                               | 30.4 ms: 1.07x slower                                                                                                       |
| pidigits                 | 257 ms                                                                                                                | 292 ms: 1.14x slower                                                                                                        |
| regex_v8                 | 24.6 ms                                                                                                               | 28.3 ms: 1.15x slower                                                                                                       |
| xml_etree_parse          | 141 ms                                                                                                                | 167 ms: 1.18x slower                                                                                                        |
| unpack_sequence          | 45.7 ns                                                                                                               | 59.9 ns: 1.31x slower                                                                                                       |
| Geometric mean           | (ref)                                                                                                                 | 1.02x faster                                                                                                                |

Benchmark hidden because not significant (7): bench_mp_pool, asyncio_websockets, pycparser, nbody, json_loads, djangocms, unpickle_list

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x