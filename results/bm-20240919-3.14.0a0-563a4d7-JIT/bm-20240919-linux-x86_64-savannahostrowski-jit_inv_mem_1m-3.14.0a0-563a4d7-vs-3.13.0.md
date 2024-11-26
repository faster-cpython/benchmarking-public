# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 563a4d7
- commit date: 2024-09-19
- overall geometric mean: 1.022x faster
- HPT reliability: 80.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                                       |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                     |
| html5lib       | 64.2 ms                                                | 65.1 ms: 1.01x slower                                                      |
| tornado_http   | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 388 ms: 1.20x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                       |
| async_tree_none           | 351 ms                                                 | 317 ms: 1.11x faster                                                       |
| async_tree_none_tg        | 321 ms                                                 | 308 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 565 ms: 1.02x faster                                                       |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 873 ms: 1.02x slower                                                       |
| coroutines                | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                      |
| async_generators          | 436 ms                                                 | 453 ms: 1.04x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.7 ms: 1.14x faster                                                      |
| nbody          | 87.0 ms                                                | 81.3 ms: 1.07x faster                                                      |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.76 ms: 1.01x slower                                                      |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 78.0 ms: 1.11x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| json_dumps           | 10.6 ms                                                | 9.88 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.03x faster                                                      |
| pickle_pure_python   | 310 us                                                 | 305 us: 1.02x faster                                                       |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                      |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                      |
| django_template | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                      |
| genshi_text     | 23.5 ms                                                | 25.8 ms: 1.10x slower                                                      |
| genshi_xml      | 50.9 ms                                                | 61.2 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.5 us: 1.42x faster                                                      |
| create_gc_cycles          | 2.41 ms                                                | 1.74 ms: 1.38x faster                                                      |
| deepcopy                  | 358 us                                                 | 269 us: 1.33x faster                                                       |
| async_tree_memoization_tg | 464 ms                                                 | 388 ms: 1.20x faster                                                       |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                      |
| scimark_fft               | 364 ms                                                 | 309 ms: 1.18x faster                                                       |
| deepcopy_reduce           | 3.20 us                                                | 2.74 us: 1.17x faster                                                      |
| gc_traversal              | 4.37 ms                                                | 3.74 ms: 1.17x faster                                                      |
| richards                  | 48.7 ms                                                | 41.9 ms: 1.16x faster                                                      |
| richards_super            | 54.9 ms                                                | 47.7 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.39 ms: 1.15x faster                                                      |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                       |
| float                     | 79.2 ms                                                | 69.7 ms: 1.14x faster                                                      |
| crypto_pyaes              | 75.3 ms                                                | 66.3 ms: 1.14x faster                                                      |
| mako                      | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                      |
| xml_etree_generate        | 86.7 ms                                                | 78.0 ms: 1.11x faster                                                      |
| async_tree_none           | 351 ms                                                 | 317 ms: 1.11x faster                                                       |
| tomli_loads               | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                     |
| pathlib                   | 17.5 ms                                                | 16.0 ms: 1.09x faster                                                      |
| go                        | 144 ms                                                 | 133 ms: 1.08x faster                                                       |
| fannkuch                  | 404 ms                                                 | 374 ms: 1.08x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| telco                     | 8.54 ms                                                | 7.98 ms: 1.07x faster                                                      |
| nbody                     | 87.0 ms                                                | 81.3 ms: 1.07x faster                                                      |
| json_dumps                | 10.6 ms                                                | 9.88 ms: 1.07x faster                                                      |
| json                      | 5.36 ms                                                | 5.03 ms: 1.07x faster                                                      |
| scimark_monte_carlo       | 67.4 ms                                                | 63.4 ms: 1.06x faster                                                      |
| regex_v8                  | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                      |
| bpe_tokeniser             | 4.75 sec                                               | 4.49 sec: 1.06x faster                                                     |
| scimark_sor               | 124 ms                                                 | 117 ms: 1.05x faster                                                       |
| async_tree_none_tg        | 321 ms                                                 | 308 ms: 1.04x faster                                                       |
| logging_format            | 6.40 us                                                | 6.18 us: 1.03x faster                                                      |
| thrift                    | 809 us                                                 | 788 us: 1.03x faster                                                       |
| xml_etree_iterparse       | 101 ms                                                 | 98.8 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 565 ms: 1.02x faster                                                       |
| pickle_pure_python        | 310 us                                                 | 305 us: 1.02x faster                                                       |
| json_loads                | 27.2 us                                                | 26.9 us: 1.01x faster                                                      |
| scimark_lu                | 113 ms                                                 | 111 ms: 1.01x faster                                                       |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.01x faster                                                       |
| logging_simple            | 5.72 us                                                | 5.67 us: 1.01x faster                                                      |
| pycparser                 | 1.20 sec                                               | 1.19 sec: 1.01x faster                                                     |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| deltablue                 | 3.23 ms                                                | 3.24 ms: 1.00x slower                                                      |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                       |
| regex_effbot              | 3.73 ms                                                | 3.76 ms: 1.01x slower                                                      |
| unpickle_pure_python      | 216 us                                                 | 217 us: 1.01x slower                                                       |
| chaos                     | 58.1 ms                                                | 58.6 ms: 1.01x slower                                                      |
| typing_runtime_protocols  | 165 us                                                 | 167 us: 1.01x slower                                                       |
| python_startup_no_site    | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                      |
| html5lib                  | 64.2 ms                                                | 65.1 ms: 1.01x slower                                                      |
| async_tree_io_tg          | 857 ms                                                 | 873 ms: 1.02x slower                                                       |
| bench_thread_pool         | 822 us                                                 | 840 us: 1.02x slower                                                       |
| tornado_http              | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                      |
| pprint_safe_repr          | 728 ms                                                 | 745 ms: 1.02x slower                                                       |
| django_template           | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                      |
| coroutines                | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                      |
| logging_silent            | 102 ns                                                 | 105 ns: 1.03x slower                                                       |
| comprehensions            | 16.5 us                                                | 17.1 us: 1.04x slower                                                      |
| 2to3                      | 267 ms                                                 | 277 ms: 1.04x slower                                                       |
| async_generators          | 436 ms                                                 | 453 ms: 1.04x slower                                                       |
| pprint_pformat            | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                     |
| raytrace                  | 267 ms                                                 | 279 ms: 1.04x slower                                                       |
| sqlglot_normalize         | 108 ms                                                 | 112 ms: 1.04x slower                                                       |
| coverage                  | 84.0 ms                                                | 88.0 ms: 1.05x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                      |
| dulwich_log               | 64.3 ms                                                | 68.5 ms: 1.07x slower                                                      |
| sqlglot_transpile         | 1.58 ms                                                | 1.70 ms: 1.07x slower                                                      |
| sqlglot_optimize          | 53.7 ms                                                | 58.4 ms: 1.09x slower                                                      |
| regex_compile             | 132 ms                                                 | 144 ms: 1.09x slower                                                       |
| genshi_text               | 23.5 ms                                                | 25.8 ms: 1.10x slower                                                      |
| sympy_expand              | 463 ms                                                 | 513 ms: 1.11x slower                                                       |
| sympy_str                 | 275 ms                                                 | 305 ms: 1.11x slower                                                       |
| nqueens                   | 78.4 ms                                                | 88.8 ms: 1.13x slower                                                      |
| docutils                  | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                     |
| hexiom                    | 6.16 ms                                                | 7.07 ms: 1.15x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 174 ms: 1.16x slower                                                       |
| genshi_xml                | 50.9 ms                                                | 61.2 ms: 1.20x slower                                                      |
| pylint                    | 313 ms                                                 | 377 ms: 1.21x slower                                                       |
| generators                | 29.0 ms                                                | 36.2 ms: 1.25x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (6): regex_dna, mdp, pyflate, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240919-3.14.0a0-563a4d7-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.022x faster
# HPT report

- Reliability score: 80.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x