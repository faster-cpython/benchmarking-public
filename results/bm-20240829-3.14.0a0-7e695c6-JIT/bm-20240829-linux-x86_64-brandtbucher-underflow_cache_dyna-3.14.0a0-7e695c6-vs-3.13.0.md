# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_cache_dyna
- machine: linux-x86_64
- commit hash: 7e695c6
- commit date: 2024-08-29
- overall geometric mean: 1.005x faster
- HPT reliability: 57.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 282 ms: 1.06x slower                                                        |
| docutils       | 2.59 sec                                               | 3.30 sec: 1.27x slower                                                      |
| html5lib       | 64.2 ms                                                | 76.2 ms: 1.19x slower                                                       |
| tornado_http   | 92.4 ms                                                | 99.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.15x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 410 ms: 1.13x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 411 ms: 1.08x faster                                                        |
| async_tree_none           | 351 ms                                                 | 328 ms: 1.07x faster                                                        |
| async_tree_none_tg        | 321 ms                                                 | 314 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 565 ms: 1.02x faster                                                        |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                        |
| coroutines                | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 901 ms: 1.05x slower                                                        |
| async_generators          | 436 ms                                                 | 465 ms: 1.07x slower                                                        |
| async_tree_io             | 842 ms                                                 | 936 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.1 ms: 1.11x faster                                                       |
| nbody          | 87.0 ms                                                | 79.3 ms: 1.10x faster                                                       |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                       |
| regex_effbot   | 3.73 ms                                                | 3.76 ms: 1.01x slower                                                       |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                        |
| regex_compile  | 132 ms                                                 | 154 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.1 ms: 1.13x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 54.8 ms: 1.11x faster                                                       |
| tomli_loads          | 2.14 sec                                               | 1.99 sec: 1.07x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| json_dumps           | 10.6 ms                                                | 9.94 ms: 1.06x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 203 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                                       |
| json_loads           | 27.2 us                                                | 29.5 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                       |
| genshi_text     | 23.5 ms                                                | 23.1 ms: 1.02x faster                                                       |
| django_template | 35.2 ms                                                | 38.9 ms: 1.11x slower                                                       |
| genshi_xml      | 50.9 ms                                                | 64.0 ms: 1.26x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.1 us: 1.50x faster                                                       |
| create_gc_cycles          | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                       |
| deepcopy                  | 358 us                                                 | 267 us: 1.34x faster                                                        |
| richards                  | 48.7 ms                                                | 40.4 ms: 1.21x faster                                                       |
| richards_super            | 54.9 ms                                                | 45.8 ms: 1.20x faster                                                       |
| deepcopy_reduce           | 3.20 us                                                | 2.68 us: 1.19x faster                                                       |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                       |
| scimark_fft               | 364 ms                                                 | 315 ms: 1.16x faster                                                        |
| gc_traversal              | 4.37 ms                                                | 3.78 ms: 1.16x faster                                                       |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.40 ms: 1.15x faster                                                       |
| mako                      | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                       |
| async_tree_memoization_tg | 464 ms                                                 | 410 ms: 1.13x faster                                                        |
| xml_etree_generate        | 86.7 ms                                                | 77.1 ms: 1.13x faster                                                       |
| scimark_lu                | 113 ms                                                 | 101 ms: 1.12x faster                                                        |
| crypto_pyaes              | 75.3 ms                                                | 67.5 ms: 1.12x faster                                                       |
| float                     | 79.2 ms                                                | 71.1 ms: 1.11x faster                                                       |
| telco                     | 8.54 ms                                                | 7.69 ms: 1.11x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 54.8 ms: 1.11x faster                                                       |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                       |
| nbody                     | 87.0 ms                                                | 79.3 ms: 1.10x faster                                                       |
| scimark_monte_carlo       | 67.4 ms                                                | 61.7 ms: 1.09x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 411 ms: 1.08x faster                                                        |
| tomli_loads               | 2.14 sec                                               | 1.99 sec: 1.07x faster                                                      |
| logging_silent            | 102 ns                                                 | 94.7 ns: 1.07x faster                                                       |
| regex_v8                  | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                       |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| bpe_tokeniser             | 4.75 sec                                               | 4.44 sec: 1.07x faster                                                      |
| async_tree_none           | 351 ms                                                 | 328 ms: 1.07x faster                                                        |
| fannkuch                  | 404 ms                                                 | 380 ms: 1.06x faster                                                        |
| json_dumps                | 10.6 ms                                                | 9.94 ms: 1.06x faster                                                       |
| unpickle_pure_python      | 216 us                                                 | 203 us: 1.06x faster                                                        |
| pyflate                   | 471 ms                                                 | 454 ms: 1.04x faster                                                        |
| xml_etree_iterparse       | 101 ms                                                 | 98.5 ms: 1.03x faster                                                       |
| async_tree_none_tg        | 321 ms                                                 | 314 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 565 ms: 1.02x faster                                                        |
| genshi_text               | 23.5 ms                                                | 23.1 ms: 1.02x faster                                                       |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                        |
| thrift                    | 809 us                                                 | 795 us: 1.02x faster                                                        |
| logging_format            | 6.40 us                                                | 6.29 us: 1.02x faster                                                       |
| json                      | 5.36 ms                                                | 5.28 ms: 1.02x faster                                                       |
| pprint_pformat            | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                      |
| typing_runtime_protocols  | 165 us                                                 | 164 us: 1.01x faster                                                        |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| regex_effbot              | 3.73 ms                                                | 3.76 ms: 1.01x slower                                                       |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                        |
| bench_thread_pool         | 822 us                                                 | 830 us: 1.01x slower                                                        |
| regex_dna                 | 218 ms                                                 | 221 ms: 1.01x slower                                                        |
| deltablue                 | 3.23 ms                                                | 3.27 ms: 1.02x slower                                                       |
| coroutines                | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                       |
| chaos                     | 58.1 ms                                                | 59.6 ms: 1.03x slower                                                       |
| python_startup_no_site    | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                       |
| coverage                  | 84.0 ms                                                | 87.4 ms: 1.04x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 901 ms: 1.05x slower                                                        |
| raytrace                  | 267 ms                                                 | 282 ms: 1.06x slower                                                        |
| 2to3                      | 267 ms                                                 | 282 ms: 1.06x slower                                                        |
| async_generators          | 436 ms                                                 | 465 ms: 1.07x slower                                                        |
| nqueens                   | 78.4 ms                                                | 83.8 ms: 1.07x slower                                                       |
| tornado_http              | 92.4 ms                                                | 99.5 ms: 1.08x slower                                                       |
| json_loads                | 27.2 us                                                | 29.5 us: 1.09x slower                                                       |
| django_template           | 35.2 ms                                                | 38.9 ms: 1.11x slower                                                       |
| sqlglot_optimize          | 53.7 ms                                                | 59.7 ms: 1.11x slower                                                       |
| async_tree_io             | 842 ms                                                 | 936 ms: 1.11x slower                                                        |
| sqlglot_normalize         | 108 ms                                                 | 120 ms: 1.12x slower                                                        |
| sqlglot_transpile         | 1.58 ms                                                | 1.80 ms: 1.14x slower                                                       |
| sympy_expand              | 463 ms                                                 | 528 ms: 1.14x slower                                                        |
| hexiom                    | 6.16 ms                                                | 7.04 ms: 1.14x slower                                                       |
| sympy_str                 | 275 ms                                                 | 321 ms: 1.17x slower                                                        |
| regex_compile             | 132 ms                                                 | 154 ms: 1.17x slower                                                        |
| pycparser                 | 1.20 sec                                               | 1.42 sec: 1.18x slower                                                      |
| generators                | 29.0 ms                                                | 34.3 ms: 1.18x slower                                                       |
| html5lib                  | 64.2 ms                                                | 76.2 ms: 1.19x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 23.7 ms: 1.19x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 180 ms: 1.19x slower                                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.53 ms: 1.20x slower                                                       |
| go                        | 144 ms                                                 | 173 ms: 1.20x slower                                                        |
| scimark_sor               | 124 ms                                                 | 154 ms: 1.24x slower                                                        |
| genshi_xml                | 50.9 ms                                                | 64.0 ms: 1.26x slower                                                       |
| docutils                  | 2.59 sec                                               | 3.30 sec: 1.27x slower                                                      |
| pylint                    | 313 ms                                                 | 406 ms: 1.30x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (6): pprint_safe_repr, pickle_pure_python, bench_mp_pool, logging_simple, async_tree_cpu_io_mixed_tg, comprehensions
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-7e695c6-JIT/bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.005x faster
# HPT report

- Reliability score: 57.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x