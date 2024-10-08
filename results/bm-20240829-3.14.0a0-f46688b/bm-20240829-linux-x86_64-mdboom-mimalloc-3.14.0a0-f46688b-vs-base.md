# Results vs. base

- fork: mdboom
- ref: mimalloc
- machine: linux-x86_64
- commit hash: f46688b
- commit date: 2024-08-29
- overall geometric mean: 1.01x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 251 ms: 1.02x faster                                      |
| docutils       | 2.66 sec                                                              | 2.67 sec: 1.00x slower                                    |
| html5lib       | 63.5 ms                                                               | 61.9 ms: 1.03x faster                                     |
| tornado_http   | 90.4 ms                                                               | 86.9 ms: 1.04x faster                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| asyncio_websockets      | 557 ms                                                                | 542 ms: 1.03x faster                                      |
| async_tree_none_tg      | 309 ms                                                                | 304 ms: 1.02x faster                                      |
| coroutines              | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                     |
| async_generators        | 431 ms                                                                | 437 ms: 1.02x slower                                      |
| asyncio_tcp             | 486 ms                                                                | 496 ms: 1.02x slower                                      |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.83 sec: 1.02x slower                                    |
| async_tree_cpu_io_mixed | 557 ms                                                                | 569 ms: 1.02x slower                                      |
| async_tree_io_tg        | 900 ms                                                                | 948 ms: 1.05x slower                                      |
| async_tree_memoization  | 392 ms                                                                | 415 ms: 1.06x slower                                      |
| async_tree_io           | 931 ms                                                                | 1.00 sec: 1.07x slower                                    |
| Geometric mean          | (ref)                                                                 | 1.02x slower                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| float          | 79.2 ms                                                               | 75.7 ms: 1.05x faster                                     |
| pidigits       | 186 ms                                                                | 185 ms: 1.01x faster                                      |
| nbody          | 87.8 ms                                                               | 89.7 ms: 1.02x slower                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot   | 3.58 ms                                                               | 3.34 ms: 1.07x faster                                     |
| regex_dna      | 221 ms                                                                | 208 ms: 1.06x faster                                      |
| regex_v8       | 24.4 ms                                                               | 23.3 ms: 1.05x faster                                     |
| regex_compile  | 129 ms                                                                | 126 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                                 | 1.05x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                                              | 2.01 sec: 1.05x faster                                    |
| json_dumps           | 10.6 ms                                                               | 10.1 ms: 1.04x faster                                     |
| json_loads           | 28.6 us                                                               | 27.5 us: 1.04x faster                                     |
| xml_etree_parse      | 159 ms                                                                | 153 ms: 1.04x faster                                      |
| pickle_pure_python   | 304 us                                                                | 296 us: 1.03x faster                                      |
| xml_etree_iterparse  | 105 ms                                                                | 103 ms: 1.02x faster                                      |
| unpickle_pure_python | 215 us                                                                | 214 us: 1.00x faster                                      |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                              |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                     |
| python_startup_no_site | 7.13 ms                                                               | 7.05 ms: 1.01x faster                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 11.5 ms                                                               | 10.4 ms: 1.10x faster                                     |
| django_template | 33.9 ms                                                               | 33.2 ms: 1.02x faster                                     |
| genshi_xml      | 49.4 ms                                                               | 49.1 ms: 1.01x faster                                     |
| genshi_text     | 22.5 ms                                                               | 22.8 ms: 1.01x slower                                     |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| mako                     | 11.5 ms                                                               | 10.4 ms: 1.10x faster                                     |
| json                     | 5.34 ms                                                               | 4.97 ms: 1.07x faster                                     |
| regex_effbot             | 3.58 ms                                                               | 3.34 ms: 1.07x faster                                     |
| pyflate                  | 470 ms                                                                | 442 ms: 1.06x faster                                      |
| regex_dna                | 221 ms                                                                | 208 ms: 1.06x faster                                      |
| pycparser                | 1.14 sec                                                              | 1.08 sec: 1.06x faster                                    |
| deepcopy_reduce          | 2.75 us                                                               | 2.61 us: 1.05x faster                                     |
| pathlib                  | 16.0 ms                                                               | 15.2 ms: 1.05x faster                                     |
| scimark_fft              | 366 ms                                                                | 350 ms: 1.05x faster                                      |
| float                    | 79.2 ms                                                               | 75.7 ms: 1.05x faster                                     |
| tomli_loads              | 2.11 sec                                                              | 2.01 sec: 1.05x faster                                    |
| regex_v8                 | 24.4 ms                                                               | 23.3 ms: 1.05x faster                                     |
| json_dumps               | 10.6 ms                                                               | 10.1 ms: 1.04x faster                                     |
| crypto_pyaes             | 72.9 ms                                                               | 69.9 ms: 1.04x faster                                     |
| pprint_safe_repr         | 726 ms                                                                | 697 ms: 1.04x faster                                      |
| json_loads               | 28.6 us                                                               | 27.5 us: 1.04x faster                                     |
| tornado_http             | 90.4 ms                                                               | 86.9 ms: 1.04x faster                                     |
| spectral_norm            | 113 ms                                                                | 108 ms: 1.04x faster                                      |
| xml_etree_parse          | 159 ms                                                                | 153 ms: 1.04x faster                                      |
| deepcopy                 | 263 us                                                                | 253 us: 1.04x faster                                      |
| thrift                   | 775 us                                                                | 747 us: 1.04x faster                                      |
| scimark_sor              | 126 ms                                                                | 122 ms: 1.04x faster                                      |
| sqlglot_normalize        | 107 ms                                                                | 104 ms: 1.04x faster                                      |
| scimark_lu               | 114 ms                                                                | 111 ms: 1.03x faster                                      |
| nqueens                  | 80.2 ms                                                               | 77.9 ms: 1.03x faster                                     |
| sqlglot_optimize         | 53.6 ms                                                               | 52.1 ms: 1.03x faster                                     |
| asyncio_websockets       | 557 ms                                                                | 542 ms: 1.03x faster                                      |
| gc_traversal             | 3.72 ms                                                               | 3.62 ms: 1.03x faster                                     |
| pickle_pure_python       | 304 us                                                                | 296 us: 1.03x faster                                      |
| html5lib                 | 63.5 ms                                                               | 61.9 ms: 1.03x faster                                     |
| regex_compile            | 129 ms                                                                | 126 ms: 1.02x faster                                      |
| xml_etree_iterparse      | 105 ms                                                                | 103 ms: 1.02x faster                                      |
| go                       | 119 ms                                                                | 116 ms: 1.02x faster                                      |
| sympy_str                | 269 ms                                                                | 263 ms: 1.02x faster                                      |
| sqlglot_parse            | 1.29 ms                                                               | 1.26 ms: 1.02x faster                                     |
| deepcopy_memo            | 29.9 us                                                               | 29.3 us: 1.02x faster                                     |
| generators               | 28.7 ms                                                               | 28.2 ms: 1.02x faster                                     |
| sympy_sum                | 148 ms                                                                | 146 ms: 1.02x faster                                      |
| django_template          | 33.9 ms                                                               | 33.2 ms: 1.02x faster                                     |
| sympy_expand             | 456 ms                                                                | 447 ms: 1.02x faster                                      |
| async_tree_none_tg       | 309 ms                                                                | 304 ms: 1.02x faster                                      |
| 2to3                     | 256 ms                                                                | 251 ms: 1.02x faster                                      |
| pprint_pformat           | 1.47 sec                                                              | 1.44 sec: 1.02x faster                                    |
| python_startup           | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                     |
| scimark_sparse_mat_mult  | 4.92 ms                                                               | 4.84 ms: 1.02x faster                                     |
| logging_silent           | 99.9 ns                                                               | 98.5 ns: 1.01x faster                                     |
| typing_runtime_protocols | 159 us                                                                | 157 us: 1.01x faster                                      |
| scimark_monte_carlo      | 66.9 ms                                                               | 66.1 ms: 1.01x faster                                     |
| python_startup_no_site   | 7.13 ms                                                               | 7.05 ms: 1.01x faster                                     |
| create_gc_cycles         | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                     |
| sympy_integrate          | 19.7 ms                                                               | 19.5 ms: 1.01x faster                                     |
| sqlglot_transpile        | 1.58 ms                                                               | 1.57 ms: 1.01x faster                                     |
| genshi_xml               | 49.4 ms                                                               | 49.1 ms: 1.01x faster                                     |
| chaos                    | 58.9 ms                                                               | 58.5 ms: 1.01x faster                                     |
| deltablue                | 3.21 ms                                                               | 3.19 ms: 1.01x faster                                     |
| pidigits                 | 186 ms                                                                | 185 ms: 1.01x faster                                      |
| unpickle_pure_python     | 215 us                                                                | 214 us: 1.00x faster                                      |
| fannkuch                 | 401 ms                                                                | 403 ms: 1.00x slower                                      |
| docutils                 | 2.66 sec                                                              | 2.67 sec: 1.00x slower                                    |
| raytrace                 | 262 ms                                                                | 264 ms: 1.01x slower                                      |
| hexiom                   | 6.15 ms                                                               | 6.19 ms: 1.01x slower                                     |
| coroutines               | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                     |
| telco                    | 8.39 ms                                                               | 8.47 ms: 1.01x slower                                     |
| comprehensions           | 16.5 us                                                               | 16.6 us: 1.01x slower                                     |
| genshi_text              | 22.5 ms                                                               | 22.8 ms: 1.01x slower                                     |
| async_generators         | 431 ms                                                                | 437 ms: 1.02x slower                                      |
| asyncio_tcp              | 486 ms                                                                | 496 ms: 1.02x slower                                      |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.83 sec: 1.02x slower                                    |
| nbody                    | 87.8 ms                                                               | 89.7 ms: 1.02x slower                                     |
| async_tree_cpu_io_mixed  | 557 ms                                                                | 569 ms: 1.02x slower                                      |
| richards                 | 45.8 ms                                                               | 47.0 ms: 1.02x slower                                     |
| logging_simple           | 5.49 us                                                               | 5.64 us: 1.03x slower                                     |
| richards_super           | 52.1 ms                                                               | 53.5 ms: 1.03x slower                                     |
| bpe_tokeniser            | 4.80 sec                                                              | 4.96 sec: 1.03x slower                                    |
| async_tree_io_tg         | 900 ms                                                                | 948 ms: 1.05x slower                                      |
| async_tree_memoization   | 392 ms                                                                | 415 ms: 1.06x slower                                      |
| coverage                 | 84.4 ms                                                               | 89.3 ms: 1.06x slower                                     |
| async_tree_io            | 931 ms                                                                | 1.00 sec: 1.07x slower                                    |
| bench_thread_pool        | 784 us                                                                | 1.24 ms: 1.59x slower                                     |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                              |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, meteor_contest, pylint, xml_etree_generate, mdp, bench_mp_pool, xml_etree_process, logging_format, async_tree_memoization_tg, async_tree_none

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x