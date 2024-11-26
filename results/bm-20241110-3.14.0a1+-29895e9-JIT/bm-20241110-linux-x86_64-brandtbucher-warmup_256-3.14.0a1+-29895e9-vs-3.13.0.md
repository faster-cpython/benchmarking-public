# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_256
- machine: linux-x86_64
- commit hash: 29895e9
- commit date: 2024-11-10
- overall geometric mean: 1.001x faster
- HPT reliability: 79.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                               |
| docutils       | 2.59 sec                                               | 2.90 sec: 1.12x slower                                             |
| html5lib       | 64.2 ms                                                | 65.4 ms: 1.02x slower                                              |
| sphinx         | 1.03 sec                                               | 1.15 sec: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                               |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                               |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                               |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                              |
| async_tree_io              | 842 ms                                                 | 861 ms: 1.02x slower                                               |
| async_generators           | 436 ms                                                 | 449 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 569 ms: 1.04x slower                                               |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                               |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 80.9 ms: 1.08x faster                                              |
| float          | 79.2 ms                                                | 76.5 ms: 1.04x faster                                              |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                              |
| regex_dna      | 218 ms                                                 | 215 ms: 1.02x faster                                               |
| regex_effbot   | 3.73 ms                                                | 3.69 ms: 1.01x faster                                              |
| regex_compile  | 132 ms                                                 | 137 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 78.2 ms: 1.11x faster                                              |
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.10x faster                                             |
| unpickle_pure_python | 216 us                                                 | 196 us: 1.10x faster                                               |
| xml_etree_process    | 60.6 ms                                                | 55.5 ms: 1.09x faster                                              |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                               |
| json_dumps           | 10.6 ms                                                | 10.9 ms: 1.04x slower                                              |
| pickle_pure_python   | 310 us                                                 | 328 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                              |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.08x faster                                              |
| django_template | 35.2 ms                                                | 35.9 ms: 1.02x slower                                              |
| genshi_text     | 23.5 ms                                                | 25.3 ms: 1.08x slower                                              |
| genshi_xml      | 50.9 ms                                                | 57.1 ms: 1.12x slower                                              |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.5 us: 1.33x faster                                              |
| deepcopy                   | 358 us                                                 | 272 us: 1.32x faster                                               |
| richards                   | 48.7 ms                                                | 39.7 ms: 1.23x faster                                              |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                               |
| richards_super             | 54.9 ms                                                | 46.1 ms: 1.19x faster                                              |
| deepcopy_reduce            | 3.20 us                                                | 2.76 us: 1.16x faster                                              |
| scimark_fft                | 364 ms                                                 | 322 ms: 1.13x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 78.2 ms: 1.11x faster                                              |
| telco                      | 8.54 ms                                                | 7.72 ms: 1.11x faster                                              |
| crypto_pyaes               | 75.3 ms                                                | 68.1 ms: 1.11x faster                                              |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.10x faster                                             |
| unpickle_pure_python       | 216 us                                                 | 196 us: 1.10x faster                                               |
| go                         | 144 ms                                                 | 131 ms: 1.10x faster                                               |
| xml_etree_process          | 60.6 ms                                                | 55.5 ms: 1.09x faster                                              |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.08x faster                                              |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.65 ms: 1.08x faster                                              |
| nbody                      | 87.0 ms                                                | 80.9 ms: 1.08x faster                                              |
| json                       | 5.36 ms                                                | 4.99 ms: 1.07x faster                                              |
| pathlib                    | 17.5 ms                                                | 16.4 ms: 1.07x faster                                              |
| bpe_tokeniser              | 4.75 sec                                               | 4.45 sec: 1.07x faster                                             |
| mdp                        | 2.72 sec                                               | 2.55 sec: 1.07x faster                                             |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                               |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                               |
| fannkuch                   | 404 ms                                                 | 383 ms: 1.06x faster                                               |
| regex_v8                   | 26.2 ms                                                | 24.8 ms: 1.06x faster                                              |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                             |
| scimark_monte_carlo        | 67.4 ms                                                | 64.6 ms: 1.04x faster                                              |
| pyflate                    | 471 ms                                                 | 451 ms: 1.04x faster                                               |
| logging_format             | 6.40 us                                                | 6.15 us: 1.04x faster                                              |
| float                      | 79.2 ms                                                | 76.5 ms: 1.04x faster                                              |
| thrift                     | 809 us                                                 | 786 us: 1.03x faster                                               |
| logging_silent             | 102 ns                                                 | 99.5 ns: 1.02x faster                                              |
| scimark_sor                | 124 ms                                                 | 121 ms: 1.02x faster                                               |
| logging_simple             | 5.72 us                                                | 5.62 us: 1.02x faster                                              |
| regex_dna                  | 218 ms                                                 | 215 ms: 1.02x faster                                               |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                               |
| connected_components       | 444 ms                                                 | 437 ms: 1.02x faster                                               |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                               |
| regex_effbot               | 3.73 ms                                                | 3.69 ms: 1.01x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                               |
| gc_traversal               | 4.37 ms                                                | 4.38 ms: 1.00x slower                                              |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                               |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                              |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                               |
| deltablue                  | 3.23 ms                                                | 3.26 ms: 1.01x slower                                              |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                              |
| pprint_safe_repr           | 728 ms                                                 | 739 ms: 1.02x slower                                               |
| typing_runtime_protocols   | 165 us                                                 | 168 us: 1.02x slower                                               |
| html5lib                   | 64.2 ms                                                | 65.4 ms: 1.02x slower                                              |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                              |
| chaos                      | 58.1 ms                                                | 59.3 ms: 1.02x slower                                              |
| django_template            | 35.2 ms                                                | 35.9 ms: 1.02x slower                                              |
| async_tree_io              | 842 ms                                                 | 861 ms: 1.02x slower                                               |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.5 ms: 1.02x slower                                              |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                               |
| async_generators           | 436 ms                                                 | 449 ms: 1.03x slower                                               |
| shortest_path              | 481 ms                                                 | 496 ms: 1.03x slower                                               |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                             |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                              |
| json_dumps                 | 10.6 ms                                                | 10.9 ms: 1.04x slower                                              |
| regex_compile              | 132 ms                                                 | 137 ms: 1.04x slower                                               |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                              |
| 2to3                       | 267 ms                                                 | 278 ms: 1.04x slower                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 569 ms: 1.04x slower                                               |
| dulwich_log                | 64.3 ms                                                | 67.4 ms: 1.05x slower                                              |
| pickle_pure_python         | 310 us                                                 | 328 us: 1.06x slower                                               |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.06x slower                                               |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                              |
| genshi_text                | 23.5 ms                                                | 25.3 ms: 1.08x slower                                              |
| bench_thread_pool          | 822 us                                                 | 886 us: 1.08x slower                                               |
| sympy_expand               | 463 ms                                                 | 500 ms: 1.08x slower                                               |
| sqlglot_optimize           | 53.7 ms                                                | 58.1 ms: 1.08x slower                                              |
| sqlalchemy_declarative     | 133 ms                                                 | 145 ms: 1.09x slower                                               |
| sympy_str                  | 275 ms                                                 | 300 ms: 1.09x slower                                               |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.11x slower                                              |
| sphinx                     | 1.03 sec                                               | 1.15 sec: 1.12x slower                                             |
| docutils                   | 2.59 sec                                               | 2.90 sec: 1.12x slower                                             |
| nqueens                    | 78.4 ms                                                | 87.6 ms: 1.12x slower                                              |
| genshi_xml                 | 50.9 ms                                                | 57.1 ms: 1.12x slower                                              |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                               |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.14x slower                                              |
| hexiom                     | 6.16 ms                                                | 7.07 ms: 1.15x slower                                              |
| pylint                     | 313 ms                                                 | 370 ms: 1.18x slower                                               |
| generators                 | 29.0 ms                                                | 36.7 ms: 1.27x slower                                              |
| k_core                     | 2.35 sec                                               | 3.63 sec: 1.54x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 80.3 ms: 3.35x slower                                              |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (4): json_loads, coverage, async_tree_none_tg, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241110-3.14.0a1+-29895e9-JIT/bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9.json: sqlite_synth

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 79.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x