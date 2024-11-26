# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.031x faster
- HPT reliability: 92.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 274 ms: 1.03x slower                                                    |
| docutils       | 2.59 sec                                               | 2.94 sec: 1.13x slower                                                  |
| html5lib       | 64.2 ms                                                | 62.0 ms: 1.03x faster                                                   |
| tornado_http   | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                                    |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 397 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 321 ms                                                 | 308 ms: 1.04x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                    |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                    |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                    |
| async_tree_io              | 842 ms                                                 | 885 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.1 ms: 1.13x faster                                                   |
| nbody          | 87.0 ms                                                | 81.8 ms: 1.06x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.2 ms: 1.08x faster                                                   |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                                    |
| regex_effbot   | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                   |
| regex_compile  | 132 ms                                                 | 142 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 78.1 ms: 1.11x faster                                                   |
| xml_etree_process    | 60.6 ms                                                | 55.0 ms: 1.10x faster                                                   |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                   |
| pickle_pure_python   | 310 us                                                 | 307 us: 1.01x faster                                                    |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                   |
| python_startup_no_site | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                   |
| django_template | 35.2 ms                                                | 35.5 ms: 1.01x slower                                                   |
| genshi_text     | 23.5 ms                                                | 24.4 ms: 1.04x slower                                                   |
| genshi_xml      | 50.9 ms                                                | 57.2 ms: 1.12x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.7 us: 1.46x faster                                                   |
| deepcopy                   | 358 us                                                 | 261 us: 1.37x faster                                                    |
| create_gc_cycles           | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                   |
| richards_super             | 54.9 ms                                                | 44.9 ms: 1.22x faster                                                   |
| richards                   | 48.7 ms                                                | 39.8 ms: 1.22x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.65 us: 1.21x faster                                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                                    |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                   |
| scimark_fft                | 364 ms                                                 | 312 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.39 ms: 1.15x faster                                                   |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| float                      | 79.2 ms                                                | 70.1 ms: 1.13x faster                                                   |
| crypto_pyaes               | 75.3 ms                                                | 66.8 ms: 1.13x faster                                                   |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 397 ms: 1.11x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 78.1 ms: 1.11x faster                                                   |
| xml_etree_process          | 60.6 ms                                                | 55.0 ms: 1.10x faster                                                   |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                   |
| gc_traversal               | 4.37 ms                                                | 3.97 ms: 1.10x faster                                                   |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                   |
| tomli_loads                | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                  |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                                    |
| telco                      | 8.54 ms                                                | 7.86 ms: 1.09x faster                                                   |
| regex_v8                   | 26.2 ms                                                | 24.2 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 67.4 ms                                                | 62.8 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.45 sec: 1.07x faster                                                  |
| nbody                      | 87.0 ms                                                | 81.8 ms: 1.06x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.06x faster                                                    |
| logging_format             | 6.40 us                                                | 6.05 us: 1.06x faster                                                   |
| fannkuch                   | 404 ms                                                 | 384 ms: 1.05x faster                                                    |
| json                       | 5.36 ms                                                | 5.11 ms: 1.05x faster                                                   |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                   |
| mdp                        | 2.72 sec                                               | 2.60 sec: 1.05x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 308 ms: 1.04x faster                                                    |
| html5lib                   | 64.2 ms                                                | 62.0 ms: 1.03x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                  |
| scimark_lu                 | 113 ms                                                 | 109 ms: 1.03x faster                                                    |
| regex_dna                  | 218 ms                                                 | 212 ms: 1.03x faster                                                    |
| pyflate                    | 471 ms                                                 | 458 ms: 1.03x faster                                                    |
| thrift                     | 809 us                                                 | 787 us: 1.03x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                                   |
| logging_simple             | 5.72 us                                                | 5.58 us: 1.02x faster                                                   |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                    |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                                    |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                   |
| pickle_pure_python         | 310 us                                                 | 307 us: 1.01x faster                                                    |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.00x faster                                                   |
| unpickle_pure_python       | 216 us                                                 | 215 us: 1.00x faster                                                    |
| regex_effbot               | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                    |
| coverage                   | 84.0 ms                                                | 84.8 ms: 1.01x slower                                                   |
| django_template            | 35.2 ms                                                | 35.5 ms: 1.01x slower                                                   |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                    |
| bench_thread_pool          | 822 us                                                 | 841 us: 1.02x slower                                                    |
| tornado_http               | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                   |
| logging_silent             | 102 ns                                                 | 104 ns: 1.03x slower                                                    |
| chaos                      | 58.1 ms                                                | 59.7 ms: 1.03x slower                                                   |
| 2to3                       | 267 ms                                                 | 274 ms: 1.03x slower                                                    |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                  |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                                    |
| genshi_text                | 23.5 ms                                                | 24.4 ms: 1.04x slower                                                   |
| sqlglot_normalize          | 108 ms                                                 | 112 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                   |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                    |
| async_tree_io              | 842 ms                                                 | 885 ms: 1.05x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.9 ms: 1.06x slower                                                   |
| sqlglot_transpile          | 1.58 ms                                                | 1.67 ms: 1.06x slower                                                   |
| pprint_safe_repr           | 728 ms                                                 | 772 ms: 1.06x slower                                                    |
| sqlglot_optimize           | 53.7 ms                                                | 57.7 ms: 1.07x slower                                                   |
| regex_compile              | 132 ms                                                 | 142 ms: 1.08x slower                                                    |
| sympy_str                  | 275 ms                                                 | 298 ms: 1.08x slower                                                    |
| sympy_expand               | 463 ms                                                 | 502 ms: 1.08x slower                                                    |
| nqueens                    | 78.4 ms                                                | 85.6 ms: 1.09x slower                                                   |
| hexiom                     | 6.16 ms                                                | 6.87 ms: 1.11x slower                                                   |
| genshi_xml                 | 50.9 ms                                                | 57.2 ms: 1.12x slower                                                   |
| docutils                   | 2.59 sec                                               | 2.94 sec: 1.13x slower                                                  |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                                    |
| generators                 | 29.0 ms                                                | 33.1 ms: 1.14x slower                                                   |
| pylint                     | 313 ms                                                 | 370 ms: 1.19x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, json_loads, bench_mp_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 92.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x