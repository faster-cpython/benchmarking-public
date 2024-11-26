# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 062c54f
- commit date: 2024-09-23
- overall geometric mean: 1.026x faster
- HPT reliability: 87.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                                       |
| docutils       | 2.59 sec                                               | 2.93 sec: 1.13x slower                                                     |
| tornado_http   | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                       |
| async_tree_none            | 351 ms                                                 | 313 ms: 1.12x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 396 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                                       |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                       |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                       |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.6 ms: 1.14x faster                                                      |
| nbody          | 87.0 ms                                                | 84.1 ms: 1.03x faster                                                      |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                      |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                       |
| regex_effbot   | 3.73 ms                                                | 3.80 ms: 1.02x slower                                                      |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.8 ms: 1.11x faster                                                      |
| xml_etree_process    | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.11x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| json_dumps           | 10.6 ms                                                | 9.93 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                      |
| pickle_pure_python   | 310 us                                                 | 304 us: 1.02x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                      |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                      |
| django_template | 35.2 ms                                                | 36.7 ms: 1.05x slower                                                      |
| genshi_text     | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                      |
| genshi_xml      | 50.9 ms                                                | 58.7 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.1 us: 1.44x faster                                                      |
| create_gc_cycles           | 2.41 ms                                                | 1.74 ms: 1.38x faster                                                      |
| deepcopy                   | 358 us                                                 | 263 us: 1.36x faster                                                       |
| richards                   | 48.7 ms                                                | 40.7 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.68 us: 1.20x faster                                                      |
| gc_traversal               | 4.37 ms                                                | 3.66 ms: 1.19x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                       |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.26 ms: 1.18x faster                                                      |
| richards_super             | 54.9 ms                                                | 46.7 ms: 1.17x faster                                                      |
| scimark_fft                | 364 ms                                                 | 312 ms: 1.17x faster                                                       |
| float                      | 79.2 ms                                                | 69.6 ms: 1.14x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 66.7 ms: 1.13x faster                                                      |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                      |
| async_tree_none            | 351 ms                                                 | 313 ms: 1.12x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 396 ms: 1.12x faster                                                       |
| xml_etree_generate         | 86.7 ms                                                | 77.8 ms: 1.11x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                      |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.11x faster                                                     |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                      |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.10x faster                                                       |
| go                         | 144 ms                                                 | 134 ms: 1.08x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| fannkuch                   | 404 ms                                                 | 379 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 63.3 ms: 1.07x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                      |
| json_dumps                 | 10.6 ms                                                | 9.93 ms: 1.06x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.48 sec: 1.06x faster                                                     |
| telco                      | 8.54 ms                                                | 8.08 ms: 1.06x faster                                                      |
| mdp                        | 2.72 sec                                               | 2.59 sec: 1.05x faster                                                     |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                                       |
| logging_format             | 6.40 us                                                | 6.15 us: 1.04x faster                                                      |
| pyflate                    | 471 ms                                                 | 454 ms: 1.04x faster                                                       |
| thrift                     | 809 us                                                 | 782 us: 1.03x faster                                                       |
| nbody                      | 87.0 ms                                                | 84.1 ms: 1.03x faster                                                      |
| json                       | 5.36 ms                                                | 5.21 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                                      |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                      |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                                       |
| pickle_pure_python         | 310 us                                                 | 304 us: 1.02x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                     |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                       |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                       |
| typing_runtime_protocols   | 165 us                                                 | 166 us: 1.01x slower                                                       |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                      |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                       |
| coverage                   | 84.0 ms                                                | 85.0 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                      |
| chaos                      | 58.1 ms                                                | 58.9 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                       |
| regex_effbot               | 3.73 ms                                                | 3.80 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 839 us: 1.02x slower                                                       |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 745 ms: 1.02x slower                                                       |
| tornado_http               | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                      |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                                       |
| 2to3                       | 267 ms                                                 | 277 ms: 1.04x slower                                                       |
| django_template            | 35.2 ms                                                | 36.7 ms: 1.05x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                      |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                                       |
| genshi_text                | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                      |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.06x slower                                                       |
| dulwich_log                | 64.3 ms                                                | 68.2 ms: 1.06x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.70 ms: 1.07x slower                                                      |
| regex_compile              | 132 ms                                                 | 143 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 53.7 ms                                                | 58.6 ms: 1.09x slower                                                      |
| sympy_expand               | 463 ms                                                 | 514 ms: 1.11x slower                                                       |
| sympy_str                  | 275 ms                                                 | 305 ms: 1.11x slower                                                       |
| hexiom                     | 6.16 ms                                                | 6.97 ms: 1.13x slower                                                      |
| docutils                   | 2.59 sec                                               | 2.93 sec: 1.13x slower                                                     |
| nqueens                    | 78.4 ms                                                | 89.0 ms: 1.14x slower                                                      |
| genshi_xml                 | 50.9 ms                                                | 58.7 ms: 1.15x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.16x slower                                                       |
| generators                 | 29.0 ms                                                | 34.9 ms: 1.21x slower                                                      |
| pylint                     | 313 ms                                                 | 378 ms: 1.21x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, deltablue, bench_mp_pool, html5lib, json_loads, async_tree_io_tg, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-062c54f-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.026x faster
# HPT report

- Reliability score: 87.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x