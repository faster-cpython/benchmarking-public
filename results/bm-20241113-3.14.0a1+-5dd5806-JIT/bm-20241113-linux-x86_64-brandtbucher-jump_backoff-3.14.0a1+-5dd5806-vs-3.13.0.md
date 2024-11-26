# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-x86_64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.004x faster
- HPT reliability: 79.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 262 ms: 1.02x faster                                                 |
| docutils       | 2.59 sec                                               | 2.91 sec: 1.12x slower                                               |
| html5lib       | 64.2 ms                                                | 67.2 ms: 1.05x slower                                                |
| sphinx         | 1.03 sec                                               | 1.15 sec: 1.11x slower                                               |
| Geometric mean | (ref)                                                  | 1.06x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                 |
| async_tree_none            | 351 ms                                                 | 332 ms: 1.06x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                 |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                |
| async_tree_io              | 842 ms                                                 | 863 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 560 ms: 1.03x slower                                                 |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 987 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.2 ms: 1.04x faster                                                |
| nbody          | 87.0 ms                                                | 83.8 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                |
| regex_compile  | 132 ms                                                 | 134 ms: 1.01x slower                                                 |
| regex_dna      | 218 ms                                                 | 224 ms: 1.02x slower                                                 |
| regex_effbot   | 3.73 ms                                                | 3.83 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 195 us: 1.11x faster                                                 |
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                               |
| xml_etree_process    | 60.6 ms                                                | 55.9 ms: 1.09x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 82.8 ms: 1.05x faster                                                |
| json_loads           | 27.2 us                                                | 26.3 us: 1.03x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                 |
| pickle_pure_python   | 310 us                                                 | 322 us: 1.04x slower                                                 |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                |
| django_template | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                |
| genshi_text     | 23.5 ms                                                | 25.6 ms: 1.09x slower                                                |
| genshi_xml      | 50.9 ms                                                | 59.5 ms: 1.17x slower                                                |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.2 us: 1.34x faster                                                |
| deepcopy                   | 358 us                                                 | 269 us: 1.33x faster                                                 |
| richards_super             | 54.9 ms                                                | 41.9 ms: 1.31x faster                                                |
| richards                   | 48.7 ms                                                | 37.5 ms: 1.30x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.68 us: 1.19x faster                                                |
| telco                      | 8.54 ms                                                | 7.48 ms: 1.14x faster                                                |
| scimark_fft                | 364 ms                                                 | 322 ms: 1.13x faster                                                 |
| json                       | 5.36 ms                                                | 4.83 ms: 1.11x faster                                                |
| unpickle_pure_python       | 216 us                                                 | 195 us: 1.11x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                               |
| crypto_pyaes               | 75.3 ms                                                | 69.2 ms: 1.09x faster                                                |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 55.9 ms: 1.09x faster                                                |
| go                         | 144 ms                                                 | 134 ms: 1.08x faster                                                 |
| logging_silent             | 102 ns                                                 | 95.5 ns: 1.07x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.5 ms: 1.06x faster                                                |
| regex_v8                   | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                |
| async_tree_none            | 351 ms                                                 | 332 ms: 1.06x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                               |
| bpe_tokeniser              | 4.75 sec                                               | 4.51 sec: 1.05x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                 |
| fannkuch                   | 404 ms                                                 | 385 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.80 ms: 1.05x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 82.8 ms: 1.05x faster                                                |
| pyflate                    | 471 ms                                                 | 453 ms: 1.04x faster                                                 |
| float                      | 79.2 ms                                                | 76.2 ms: 1.04x faster                                                |
| nbody                      | 87.0 ms                                                | 83.8 ms: 1.04x faster                                                |
| thrift                     | 809 us                                                 | 782 us: 1.03x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.3 us: 1.03x faster                                                |
| scimark_monte_carlo        | 67.4 ms                                                | 65.3 ms: 1.03x faster                                                |
| logging_format             | 6.40 us                                                | 6.20 us: 1.03x faster                                                |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                               |
| 2to3                       | 267 ms                                                 | 262 ms: 1.02x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.63 us: 1.02x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                 |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 728 ms                                                 | 719 ms: 1.01x faster                                                 |
| gc_traversal               | 4.37 ms                                                | 4.34 ms: 1.01x faster                                                |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                 |
| coverage                   | 84.0 ms                                                | 84.8 ms: 1.01x slower                                                |
| shortest_path              | 481 ms                                                 | 485 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                |
| regex_compile              | 132 ms                                                 | 134 ms: 1.01x slower                                                 |
| deltablue                  | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                 |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.02x slower                                                 |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.5 ms: 1.02x slower                                                |
| mdp                        | 2.72 sec                                               | 2.79 sec: 1.03x slower                                               |
| async_tree_io              | 842 ms                                                 | 863 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 560 ms: 1.03x slower                                                 |
| regex_effbot               | 3.73 ms                                                | 3.83 ms: 1.03x slower                                                |
| chaos                      | 58.1 ms                                                | 59.7 ms: 1.03x slower                                                |
| django_template            | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                |
| typing_runtime_protocols   | 165 us                                                 | 170 us: 1.03x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                |
| pickle_pure_python         | 310 us                                                 | 322 us: 1.04x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.64 ms: 1.04x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 67.2 ms: 1.04x slower                                                |
| html5lib                   | 64.2 ms                                                | 67.2 ms: 1.05x slower                                                |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 21.0 ms: 1.06x slower                                                |
| bench_thread_pool          | 822 us                                                 | 877 us: 1.07x slower                                                 |
| raytrace                   | 267 ms                                                 | 285 ms: 1.07x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.7 us: 1.07x slower                                                |
| sympy_sum                  | 150 ms                                                 | 161 ms: 1.07x slower                                                 |
| sympy_str                  | 275 ms                                                 | 295 ms: 1.07x slower                                                 |
| genshi_text                | 23.5 ms                                                | 25.6 ms: 1.09x slower                                                |
| sympy_expand               | 463 ms                                                 | 506 ms: 1.09x slower                                                 |
| pylint                     | 313 ms                                                 | 342 ms: 1.09x slower                                                 |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.11x slower                                                |
| sphinx                     | 1.03 sec                                               | 1.15 sec: 1.11x slower                                               |
| nqueens                    | 78.4 ms                                                | 87.7 ms: 1.12x slower                                                |
| docutils                   | 2.59 sec                                               | 2.91 sec: 1.12x slower                                               |
| async_tree_io_tg           | 857 ms                                                 | 987 ms: 1.15x slower                                                 |
| hexiom                     | 6.16 ms                                                | 7.15 ms: 1.16x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 59.5 ms: 1.17x slower                                                |
| generators                 | 29.0 ms                                                | 35.6 ms: 1.23x slower                                                |
| k_core                     | 2.35 sec                                               | 3.64 sec: 1.55x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, xml_etree_parse, pidigits, asyncio_websockets, connected_components, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: sqlite_synth

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 79.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x