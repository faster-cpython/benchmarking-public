# Results vs. base

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.01x slower
- HPT reliability: 92.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json | results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                                                          | 279 ms: 1.07x slower                                                                                                |
| docutils       | 2.70 sec                                                                                                        | 3.01 sec: 1.11x slower                                                                                              |
| html5lib       | 64.5 ms                                                                                                         | 67.2 ms: 1.04x slower                                                                                               |
| tornado_http   | 90.2 ms                                                                                                         | 93.4 ms: 1.04x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.07x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json | results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json |
|-------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl         | 1.79 sec                                                                                                        | 1.80 sec: 1.01x slower                                                                                              |
| coroutines              | 22.9 ms                                                                                                         | 23.4 ms: 1.02x slower                                                                                               |
| asyncio_tcp             | 487 ms                                                                                                          | 499 ms: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed | 556 ms                                                                                                          | 570 ms: 1.02x slower                                                                                                |
| async_generators        | 436 ms                                                                                                          | 452 ms: 1.04x slower                                                                                                |
| async_tree_memoization  | 397 ms                                                                                                          | 427 ms: 1.08x slower                                                                                                |
| Geometric mean          | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmark hidden because not significant (7): async_tree_io_tg, asyncio_websockets, async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json | results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 77.9 ms                                                                                                         | 70.7 ms: 1.10x faster                                                                                               |
| nbody          | 84.7 ms                                                                                                         | 80.0 ms: 1.06x faster                                                                                               |
| pidigits       | 187 ms                                                                                                          | 185 ms: 1.01x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.06x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json | results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                                                          | 221 ms: 1.01x slower                                                                                                |
| regex_v8       | 23.9 ms                                                                                                         | 24.5 ms: 1.03x slower                                                                                               |
| regex_effbot   | 3.62 ms                                                                                                         | 3.75 ms: 1.04x slower                                                                                               |
| regex_compile  | 129 ms                                                                                                          | 142 ms: 1.11x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.04x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json | results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.06 sec                                                                                                        | 1.93 sec: 1.07x faster                                                                                              |
| xml_etree_parse      | 157 ms                                                                                                          | 147 ms: 1.06x faster                                                                                                |
| xml_etree_iterparse  | 104 ms                                                                                                          | 98.4 ms: 1.06x faster                                                                                               |
| xml_etree_generate   | 86.3 ms                                                                                                         | 81.6 ms: 1.06x faster                                                                                               |
| xml_etree_process    | 59.1 ms                                                                                                         | 57.5 ms: 1.03x faster                                                                                               |
| json_dumps           | 10.4 ms                                                                                                         | 10.4 ms: 1.01x slower                                                                                               |
| pickle_pure_python   | 298 us                                                                                                          | 302 us: 1.01x slower                                                                                                |
| unpickle_pure_python | 209 us                                                                                                          | 212 us: 1.01x slower                                                                                                |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json | results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                                                                         | 10.5 ms: 1.00x slower                                                                                               |
| python_startup_no_site | 7.06 ms                                                                                                         | 7.12 ms: 1.01x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json | results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                                                                         | 9.98 ms: 1.11x faster                                                                                               |
| django_template | 33.8 ms                                                                                                         | 36.8 ms: 1.09x slower                                                                                               |
| genshi_text     | 22.5 ms                                                                                                         | 26.6 ms: 1.18x slower                                                                                               |
| genshi_xml      | 50.0 ms                                                                                                         | 59.9 ms: 1.20x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.09x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                | results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json | results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| scimark_fft              | 356 ms                                                                                                          | 308 ms: 1.15x faster                                                                                                |
| richards_super           | 51.2 ms                                                                                                         | 44.7 ms: 1.15x faster                                                                                               |
| richards                 | 45.1 ms                                                                                                         | 39.4 ms: 1.15x faster                                                                                               |
| spectral_norm            | 115 ms                                                                                                          | 102 ms: 1.12x faster                                                                                                |
| crypto_pyaes             | 74.4 ms                                                                                                         | 66.4 ms: 1.12x faster                                                                                               |
| mako                     | 11.1 ms                                                                                                         | 9.98 ms: 1.11x faster                                                                                               |
| float                    | 77.9 ms                                                                                                         | 70.7 ms: 1.10x faster                                                                                               |
| fannkuch                 | 405 ms                                                                                                          | 369 ms: 1.10x faster                                                                                                |
| scimark_sor              | 124 ms                                                                                                          | 114 ms: 1.09x faster                                                                                                |
| deepcopy_memo            | 29.1 us                                                                                                         | 27.0 us: 1.08x faster                                                                                               |
| tomli_loads              | 2.06 sec                                                                                                        | 1.93 sec: 1.07x faster                                                                                              |
| mdp                      | 2.71 sec                                                                                                        | 2.54 sec: 1.07x faster                                                                                              |
| xml_etree_parse          | 157 ms                                                                                                          | 147 ms: 1.06x faster                                                                                                |
| nbody                    | 84.7 ms                                                                                                         | 80.0 ms: 1.06x faster                                                                                               |
| xml_etree_iterparse      | 104 ms                                                                                                          | 98.4 ms: 1.06x faster                                                                                               |
| xml_etree_generate       | 86.3 ms                                                                                                         | 81.6 ms: 1.06x faster                                                                                               |
| telco                    | 8.15 ms                                                                                                         | 7.76 ms: 1.05x faster                                                                                               |
| scimark_sparse_mat_mult  | 4.52 ms                                                                                                         | 4.31 ms: 1.05x faster                                                                                               |
| pyflate                  | 466 ms                                                                                                          | 445 ms: 1.05x faster                                                                                                |
| scimark_monte_carlo      | 66.2 ms                                                                                                         | 63.6 ms: 1.04x faster                                                                                               |
| bpe_tokeniser            | 4.77 sec                                                                                                        | 4.59 sec: 1.04x faster                                                                                              |
| xml_etree_process        | 59.1 ms                                                                                                         | 57.5 ms: 1.03x faster                                                                                               |
| scimark_lu               | 111 ms                                                                                                          | 109 ms: 1.02x faster                                                                                                |
| deltablue                | 3.17 ms                                                                                                         | 3.11 ms: 1.02x faster                                                                                               |
| deepcopy_reduce          | 2.68 us                                                                                                         | 2.64 us: 1.02x faster                                                                                               |
| pidigits                 | 187 ms                                                                                                          | 185 ms: 1.01x faster                                                                                                |
| comprehensions           | 16.7 us                                                                                                         | 16.6 us: 1.01x faster                                                                                               |
| logging_format           | 6.03 us                                                                                                         | 6.00 us: 1.01x faster                                                                                               |
| python_startup           | 10.5 ms                                                                                                         | 10.5 ms: 1.00x slower                                                                                               |
| meteor_contest           | 107 ms                                                                                                          | 107 ms: 1.00x slower                                                                                                |
| create_gc_cycles         | 1.74 ms                                                                                                         | 1.75 ms: 1.01x slower                                                                                               |
| json_dumps               | 10.4 ms                                                                                                         | 10.4 ms: 1.01x slower                                                                                               |
| regex_dna                | 219 ms                                                                                                          | 221 ms: 1.01x slower                                                                                                |
| json                     | 5.28 ms                                                                                                         | 5.32 ms: 1.01x slower                                                                                               |
| python_startup_no_site   | 7.06 ms                                                                                                         | 7.12 ms: 1.01x slower                                                                                               |
| pprint_safe_repr         | 736 ms                                                                                                          | 743 ms: 1.01x slower                                                                                                |
| asyncio_tcp_ssl          | 1.79 sec                                                                                                        | 1.80 sec: 1.01x slower                                                                                              |
| pickle_pure_python       | 298 us                                                                                                          | 302 us: 1.01x slower                                                                                                |
| unpickle_pure_python     | 209 us                                                                                                          | 212 us: 1.01x slower                                                                                                |
| thrift                   | 784 us                                                                                                          | 797 us: 1.02x slower                                                                                                |
| coroutines               | 22.9 ms                                                                                                         | 23.4 ms: 1.02x slower                                                                                               |
| deepcopy                 | 258 us                                                                                                          | 263 us: 1.02x slower                                                                                                |
| asyncio_tcp              | 487 ms                                                                                                          | 499 ms: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed  | 556 ms                                                                                                          | 570 ms: 1.02x slower                                                                                                |
| regex_v8                 | 23.9 ms                                                                                                         | 24.5 ms: 1.03x slower                                                                                               |
| pprint_pformat           | 1.50 sec                                                                                                        | 1.54 sec: 1.03x slower                                                                                              |
| gc_traversal             | 3.57 ms                                                                                                         | 3.67 ms: 1.03x slower                                                                                               |
| sqlglot_parse            | 1.28 ms                                                                                                         | 1.32 ms: 1.03x slower                                                                                               |
| tornado_http             | 90.2 ms                                                                                                         | 93.4 ms: 1.04x slower                                                                                               |
| async_generators         | 436 ms                                                                                                          | 452 ms: 1.04x slower                                                                                                |
| bench_thread_pool        | 787 us                                                                                                          | 817 us: 1.04x slower                                                                                                |
| regex_effbot             | 3.62 ms                                                                                                         | 3.75 ms: 1.04x slower                                                                                               |
| html5lib                 | 64.5 ms                                                                                                         | 67.2 ms: 1.04x slower                                                                                               |
| coverage                 | 83.9 ms                                                                                                         | 87.5 ms: 1.04x slower                                                                                               |
| raytrace                 | 253 ms                                                                                                          | 264 ms: 1.04x slower                                                                                                |
| go                       | 138 ms                                                                                                          | 145 ms: 1.05x slower                                                                                                |
| logging_silent           | 96.5 ns                                                                                                         | 101 ns: 1.05x slower                                                                                                |
| pycparser                | 1.13 sec                                                                                                        | 1.20 sec: 1.06x slower                                                                                              |
| sqlglot_normalize        | 107 ms                                                                                                          | 113 ms: 1.06x slower                                                                                                |
| sqlglot_transpile        | 1.57 ms                                                                                                         | 1.68 ms: 1.07x slower                                                                                               |
| typing_runtime_protocols | 162 us                                                                                                          | 174 us: 1.07x slower                                                                                                |
| 2to3                     | 260 ms                                                                                                          | 279 ms: 1.07x slower                                                                                                |
| async_tree_memoization   | 397 ms                                                                                                          | 427 ms: 1.08x slower                                                                                                |
| nqueens                  | 78.7 ms                                                                                                         | 85.2 ms: 1.08x slower                                                                                               |
| sqlglot_optimize         | 53.1 ms                                                                                                         | 57.8 ms: 1.09x slower                                                                                               |
| django_template          | 33.8 ms                                                                                                         | 36.8 ms: 1.09x slower                                                                                               |
| sympy_expand             | 460 ms                                                                                                          | 506 ms: 1.10x slower                                                                                                |
| hexiom                   | 6.17 ms                                                                                                         | 6.81 ms: 1.10x slower                                                                                               |
| regex_compile            | 129 ms                                                                                                          | 142 ms: 1.11x slower                                                                                                |
| sympy_str                | 271 ms                                                                                                          | 301 ms: 1.11x slower                                                                                                |
| docutils                 | 2.70 sec                                                                                                        | 3.01 sec: 1.11x slower                                                                                              |
| sympy_sum                | 151 ms                                                                                                          | 175 ms: 1.16x slower                                                                                                |
| pylint                   | 317 ms                                                                                                          | 368 ms: 1.16x slower                                                                                                |
| sympy_integrate          | 19.7 ms                                                                                                         | 22.9 ms: 1.16x slower                                                                                               |
| generators               | 27.7 ms                                                                                                         | 32.6 ms: 1.18x slower                                                                                               |
| genshi_text              | 22.5 ms                                                                                                         | 26.6 ms: 1.18x slower                                                                                               |
| genshi_xml               | 50.0 ms                                                                                                         | 59.9 ms: 1.20x slower                                                                                               |
| Geometric mean           | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (12): async_tree_io_tg, pathlib, asyncio_websockets, chaos, bench_mp_pool, logging_simple, json_loads, async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 92.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x