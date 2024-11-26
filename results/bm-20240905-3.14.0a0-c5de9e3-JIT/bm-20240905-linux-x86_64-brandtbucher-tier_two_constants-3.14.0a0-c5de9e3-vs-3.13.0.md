# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c5de9e3
- commit date: 2024-09-05
- overall geometric mean: 1.029x faster
- HPT reliability: 94.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 274 ms: 1.03x slower                                                      |
| docutils       | 2.59 sec                                               | 3.02 sec: 1.16x slower                                                    |
| tornado_http   | 92.4 ms                                                | 95.5 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 402 ms: 1.15x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                      |
| async_tree_none           | 351 ms                                                 | 327 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 556 ms: 1.04x faster                                                      |
| async_tree_none_tg        | 321 ms                                                 | 311 ms: 1.03x faster                                                      |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                      |
| async_generators          | 436 ms                                                 | 453 ms: 1.04x slower                                                      |
| async_tree_io_tg          | 857 ms                                                 | 919 ms: 1.07x slower                                                      |
| async_tree_io             | 842 ms                                                 | 932 ms: 1.11x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.4 ms: 1.11x faster                                                     |
| nbody          | 87.0 ms                                                | 80.7 ms: 1.08x faster                                                     |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                     |
| regex_effbot   | 3.73 ms                                                | 3.64 ms: 1.03x faster                                                     |
| regex_dna      | 218 ms                                                 | 215 ms: 1.01x faster                                                      |
| regex_compile  | 132 ms                                                 | 140 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.6 ms: 1.12x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.12x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 54.7 ms: 1.11x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| pickle_pure_python   | 310 us                                                 | 298 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| unpickle_pure_python | 216 us                                                 | 211 us: 1.02x faster                                                      |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                     |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.18 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.86 ms: 1.12x faster                                                     |
| django_template | 35.2 ms                                                | 35.5 ms: 1.01x slower                                                     |
| genshi_text     | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 59.4 ms: 1.17x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.6 us: 1.47x faster                                                     |
| create_gc_cycles          | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                     |
| deepcopy                  | 358 us                                                 | 266 us: 1.35x faster                                                      |
| richards                  | 48.7 ms                                                | 39.1 ms: 1.24x faster                                                     |
| richards_super            | 54.9 ms                                                | 44.9 ms: 1.22x faster                                                     |
| gc_traversal              | 4.37 ms                                                | 3.62 ms: 1.21x faster                                                     |
| deepcopy_reduce           | 3.20 us                                                | 2.65 us: 1.21x faster                                                     |
| scimark_fft               | 364 ms                                                 | 307 ms: 1.19x faster                                                      |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                     |
| spectral_norm             | 115 ms                                                 | 99.1 ms: 1.16x faster                                                     |
| async_tree_memoization_tg | 464 ms                                                 | 402 ms: 1.15x faster                                                      |
| crypto_pyaes              | 75.3 ms                                                | 66.2 ms: 1.14x faster                                                     |
| mako                      | 11.1 ms                                                | 9.86 ms: 1.12x faster                                                     |
| xml_etree_generate        | 86.7 ms                                                | 77.6 ms: 1.12x faster                                                     |
| tomli_loads               | 2.14 sec                                               | 1.92 sec: 1.12x faster                                                    |
| float                     | 79.2 ms                                                | 71.4 ms: 1.11x faster                                                     |
| go                        | 144 ms                                                 | 130 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.55 ms: 1.11x faster                                                     |
| xml_etree_process         | 60.6 ms                                                | 54.7 ms: 1.11x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                      |
| pathlib                   | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                     |
| fannkuch                  | 404 ms                                                 | 372 ms: 1.09x faster                                                      |
| telco                     | 8.54 ms                                                | 7.89 ms: 1.08x faster                                                     |
| scimark_monte_carlo       | 67.4 ms                                                | 62.5 ms: 1.08x faster                                                     |
| nbody                     | 87.0 ms                                                | 80.7 ms: 1.08x faster                                                     |
| bpe_tokeniser             | 4.75 sec                                               | 4.41 sec: 1.07x faster                                                    |
| mdp                       | 2.72 sec                                               | 2.53 sec: 1.07x faster                                                    |
| regex_v8                  | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                     |
| async_tree_none           | 351 ms                                                 | 327 ms: 1.07x faster                                                      |
| scimark_sor               | 124 ms                                                 | 116 ms: 1.07x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| pyflate                   | 471 ms                                                 | 451 ms: 1.04x faster                                                      |
| thrift                    | 809 us                                                 | 776 us: 1.04x faster                                                      |
| pickle_pure_python        | 310 us                                                 | 298 us: 1.04x faster                                                      |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 556 ms: 1.04x faster                                                      |
| async_tree_none_tg        | 321 ms                                                 | 311 ms: 1.03x faster                                                      |
| xml_etree_iterparse       | 101 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| regex_effbot              | 3.73 ms                                                | 3.64 ms: 1.03x faster                                                     |
| logging_format            | 6.40 us                                                | 6.24 us: 1.02x faster                                                     |
| logging_silent            | 102 ns                                                 | 99.5 ns: 1.02x faster                                                     |
| unpickle_pure_python      | 216 us                                                 | 211 us: 1.02x faster                                                      |
| pprint_safe_repr          | 728 ms                                                 | 713 ms: 1.02x faster                                                      |
| pycparser                 | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                    |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                      |
| json_dumps                | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                     |
| regex_dna                 | 218 ms                                                 | 215 ms: 1.01x faster                                                      |
| typing_runtime_protocols  | 165 us                                                 | 162 us: 1.01x faster                                                      |
| deltablue                 | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                     |
| logging_simple            | 5.72 us                                                | 5.65 us: 1.01x faster                                                     |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                      |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                      |
| django_template           | 35.2 ms                                                | 35.5 ms: 1.01x slower                                                     |
| comprehensions            | 16.5 us                                                | 16.7 us: 1.01x slower                                                     |
| bench_thread_pool         | 822 us                                                 | 833 us: 1.01x slower                                                      |
| 2to3                      | 267 ms                                                 | 274 ms: 1.03x slower                                                      |
| python_startup_no_site    | 6.96 ms                                                | 7.18 ms: 1.03x slower                                                     |
| tornado_http              | 92.4 ms                                                | 95.5 ms: 1.03x slower                                                     |
| raytrace                  | 267 ms                                                 | 276 ms: 1.04x slower                                                      |
| async_generators          | 436 ms                                                 | 453 ms: 1.04x slower                                                      |
| sqlglot_normalize         | 108 ms                                                 | 112 ms: 1.04x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                     |
| json_loads                | 27.2 us                                                | 28.6 us: 1.05x slower                                                     |
| regex_compile             | 132 ms                                                 | 140 ms: 1.06x slower                                                      |
| dulwich_log               | 64.3 ms                                                | 68.1 ms: 1.06x slower                                                     |
| genshi_text               | 23.5 ms                                                | 24.9 ms: 1.06x slower                                                     |
| sqlglot_transpile         | 1.58 ms                                                | 1.68 ms: 1.06x slower                                                     |
| async_tree_io_tg          | 857 ms                                                 | 919 ms: 1.07x slower                                                      |
| sqlglot_optimize          | 53.7 ms                                                | 58.3 ms: 1.08x slower                                                     |
| nqueens                   | 78.4 ms                                                | 85.2 ms: 1.09x slower                                                     |
| sympy_str                 | 275 ms                                                 | 300 ms: 1.09x slower                                                      |
| sympy_expand              | 463 ms                                                 | 507 ms: 1.09x slower                                                      |
| async_tree_io             | 842 ms                                                 | 932 ms: 1.11x slower                                                      |
| hexiom                    | 6.16 ms                                                | 6.85 ms: 1.11x slower                                                     |
| coverage                  | 84.0 ms                                                | 94.0 ms: 1.12x slower                                                     |
| generators                | 29.0 ms                                                | 33.1 ms: 1.14x slower                                                     |
| sympy_integrate           | 19.9 ms                                                | 22.8 ms: 1.14x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 173 ms: 1.15x slower                                                      |
| docutils                  | 2.59 sec                                               | 3.02 sec: 1.16x slower                                                    |
| genshi_xml                | 50.9 ms                                                | 59.4 ms: 1.17x slower                                                     |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, json, pprint_pformat, coroutines, bench_mp_pool, html5lib, scimark_lu, chaos
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240905-3.14.0a0-c5de9e3-JIT/bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 94.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x