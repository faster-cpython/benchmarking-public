# Results vs. 3.13.0

- fork: brandtbucher
- ref: cache_dynamic_exits
- machine: linux-x86_64
- commit hash: 55bff1c
- commit date: 2024-08-28
- overall geometric mean: 1.026x faster
- HPT reliability: 86.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 274 ms: 1.03x slower                                                       |
| docutils       | 2.59 sec                                               | 3.05 sec: 1.17x slower                                                     |
| html5lib       | 64.2 ms                                                | 66.8 ms: 1.04x slower                                                      |
| tornado_http   | 92.4 ms                                                | 94.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 403 ms: 1.15x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 398 ms: 1.11x faster                                                       |
| async_tree_none           | 351 ms                                                 | 322 ms: 1.09x faster                                                       |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 561 ms: 1.03x faster                                                       |
| coroutines                | 22.7 ms                                                | 22.5 ms: 1.01x faster                                                      |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 897 ms: 1.05x slower                                                       |
| async_generators          | 436 ms                                                 | 461 ms: 1.06x slower                                                       |
| async_tree_io             | 842 ms                                                 | 933 ms: 1.11x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.5 ms: 1.12x faster                                                      |
| nbody          | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                      |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.08x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.56 ms: 1.05x faster                                                      |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                       |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 76.6 ms: 1.13x faster                                                      |
| xml_etree_process    | 60.6 ms                                                | 54.2 ms: 1.12x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.10x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.06x faster                                                       |
| json_dumps           | 10.6 ms                                                | 9.99 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                                      |
| pickle_pure_python   | 310 us                                                 | 305 us: 1.02x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                                       |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                      |
| python_startup_no_site | 6.96 ms                                                | 7.14 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                      |
| genshi_text     | 23.5 ms                                                | 23.8 ms: 1.01x slower                                                      |
| django_template | 35.2 ms                                                | 37.7 ms: 1.07x slower                                                      |
| genshi_xml      | 50.9 ms                                                | 56.4 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.1 us: 1.44x faster                                                      |
| create_gc_cycles          | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                      |
| deepcopy                  | 358 us                                                 | 269 us: 1.33x faster                                                       |
| richards                  | 48.7 ms                                                | 39.6 ms: 1.23x faster                                                      |
| richards_super            | 54.9 ms                                                | 45.4 ms: 1.21x faster                                                      |
| deepcopy_reduce           | 3.20 us                                                | 2.69 us: 1.19x faster                                                      |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                      |
| scimark_fft               | 364 ms                                                 | 311 ms: 1.17x faster                                                       |
| gc_traversal              | 4.37 ms                                                | 3.75 ms: 1.17x faster                                                      |
| async_tree_memoization_tg | 464 ms                                                 | 403 ms: 1.15x faster                                                       |
| crypto_pyaes              | 75.3 ms                                                | 65.9 ms: 1.14x faster                                                      |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.44 ms: 1.14x faster                                                      |
| xml_etree_generate        | 86.7 ms                                                | 76.6 ms: 1.13x faster                                                      |
| mako                      | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                      |
| float                     | 79.2 ms                                                | 70.5 ms: 1.12x faster                                                      |
| xml_etree_process         | 60.6 ms                                                | 54.2 ms: 1.12x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 398 ms: 1.11x faster                                                       |
| pathlib                   | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                      |
| tomli_loads               | 2.14 sec                                               | 1.94 sec: 1.10x faster                                                     |
| telco                     | 8.54 ms                                                | 7.75 ms: 1.10x faster                                                      |
| fannkuch                  | 404 ms                                                 | 370 ms: 1.09x faster                                                       |
| nbody                     | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                      |
| async_tree_none           | 351 ms                                                 | 322 ms: 1.09x faster                                                       |
| scimark_monte_carlo       | 67.4 ms                                                | 62.6 ms: 1.08x faster                                                      |
| regex_v8                  | 26.2 ms                                                | 24.4 ms: 1.08x faster                                                      |
| bpe_tokeniser             | 4.75 sec                                               | 4.43 sec: 1.07x faster                                                     |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                     |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.06x faster                                                       |
| pyflate                   | 471 ms                                                 | 445 ms: 1.06x faster                                                       |
| json_dumps                | 10.6 ms                                                | 9.99 ms: 1.06x faster                                                      |
| logging_format            | 6.40 us                                                | 6.06 us: 1.06x faster                                                      |
| regex_effbot              | 3.73 ms                                                | 3.56 ms: 1.05x faster                                                      |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.05x faster                                                       |
| logging_simple            | 5.72 us                                                | 5.49 us: 1.04x faster                                                      |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.03x faster                                                       |
| xml_etree_iterparse       | 101 ms                                                 | 98.3 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 561 ms: 1.03x faster                                                       |
| thrift                    | 809 us                                                 | 788 us: 1.03x faster                                                       |
| pycparser                 | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                     |
| pickle_pure_python        | 310 us                                                 | 305 us: 1.02x faster                                                       |
| json                      | 5.36 ms                                                | 5.30 ms: 1.01x faster                                                      |
| coroutines                | 22.7 ms                                                | 22.5 ms: 1.01x faster                                                      |
| deltablue                 | 3.23 ms                                                | 3.20 ms: 1.01x faster                                                      |
| regex_dna                 | 218 ms                                                 | 217 ms: 1.01x faster                                                       |
| pidigits                  | 186 ms                                                 | 185 ms: 1.01x faster                                                       |
| unpickle_pure_python      | 216 us                                                 | 215 us: 1.00x faster                                                       |
| bench_thread_pool         | 822 us                                                 | 820 us: 1.00x faster                                                       |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                       |
| scimark_lu                | 113 ms                                                 | 114 ms: 1.01x slower                                                       |
| genshi_text               | 23.5 ms                                                | 23.8 ms: 1.01x slower                                                      |
| comprehensions            | 16.5 us                                                | 16.7 us: 1.01x slower                                                      |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                       |
| tornado_http              | 92.4 ms                                                | 94.3 ms: 1.02x slower                                                      |
| python_startup_no_site    | 6.96 ms                                                | 7.14 ms: 1.03x slower                                                      |
| coverage                  | 84.0 ms                                                | 86.2 ms: 1.03x slower                                                      |
| scimark_sor               | 124 ms                                                 | 127 ms: 1.03x slower                                                       |
| 2to3                      | 267 ms                                                 | 274 ms: 1.03x slower                                                       |
| html5lib                  | 64.2 ms                                                | 66.8 ms: 1.04x slower                                                      |
| async_tree_io_tg          | 857 ms                                                 | 897 ms: 1.05x slower                                                       |
| json_loads                | 27.2 us                                                | 28.6 us: 1.05x slower                                                      |
| raytrace                  | 267 ms                                                 | 281 ms: 1.05x slower                                                       |
| sqlglot_normalize         | 108 ms                                                 | 113 ms: 1.05x slower                                                       |
| async_generators          | 436 ms                                                 | 461 ms: 1.06x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                      |
| nqueens                   | 78.4 ms                                                | 83.8 ms: 1.07x slower                                                      |
| django_template           | 35.2 ms                                                | 37.7 ms: 1.07x slower                                                      |
| sqlglot_optimize          | 53.7 ms                                                | 58.0 ms: 1.08x slower                                                      |
| regex_compile             | 132 ms                                                 | 143 ms: 1.08x slower                                                       |
| sqlglot_transpile         | 1.58 ms                                                | 1.71 ms: 1.08x slower                                                      |
| sympy_str                 | 275 ms                                                 | 299 ms: 1.09x slower                                                       |
| async_tree_io             | 842 ms                                                 | 933 ms: 1.11x slower                                                       |
| genshi_xml                | 50.9 ms                                                | 56.4 ms: 1.11x slower                                                      |
| sympy_expand              | 463 ms                                                 | 514 ms: 1.11x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 169 ms: 1.12x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 22.3 ms: 1.12x slower                                                      |
| hexiom                    | 6.16 ms                                                | 6.95 ms: 1.13x slower                                                      |
| generators                | 29.0 ms                                                | 33.9 ms: 1.17x slower                                                      |
| pylint                    | 313 ms                                                 | 367 ms: 1.17x slower                                                       |
| docutils                  | 2.59 sec                                               | 3.05 sec: 1.17x slower                                                     |
| go                        | 144 ms                                                 | 171 ms: 1.19x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, typing_runtime_protocols, pprint_safe_repr, bench_mp_pool, pprint_pformat, chaos
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-55bff1c-JIT/bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.026x faster
# HPT report

- Reliability score: 86.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x