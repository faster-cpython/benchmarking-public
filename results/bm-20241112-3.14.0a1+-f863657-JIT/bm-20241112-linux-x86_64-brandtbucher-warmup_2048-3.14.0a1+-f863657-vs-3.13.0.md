# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_2048
- machine: linux-x86_64
- commit hash: f863657
- commit date: 2024-11-12
- overall geometric mean: 1.000x faster
- HPT reliability: 89.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.59 sec                                               | 2.91 sec: 1.12x slower                                              |
| html5lib       | 64.2 ms                                                | 65.6 ms: 1.02x slower                                               |
| sphinx         | 1.03 sec                                               | 1.15 sec: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.06x slower                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                                |
| async_tree_none            | 351 ms                                                 | 333 ms: 1.05x faster                                                |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                |
| async_tree_io              | 842 ms                                                 | 862 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 559 ms: 1.02x slower                                                |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                               |
| async_generators           | 436 ms                                                 | 452 ms: 1.04x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 964 ms: 1.13x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 81.9 ms: 1.06x faster                                               |
| float          | 79.2 ms                                                | 76.0 ms: 1.04x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                               |
| regex_effbot   | 3.73 ms                                                | 3.72 ms: 1.00x faster                                               |
| regex_compile  | 132 ms                                                 | 135 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 79.3 ms: 1.09x faster                                               |
| tomli_loads          | 2.14 sec                                               | 1.97 sec: 1.08x faster                                              |
| xml_etree_process    | 60.6 ms                                                | 56.2 ms: 1.08x faster                                               |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                               |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                |
| json_dumps           | 10.6 ms                                                | 10.9 ms: 1.04x slower                                               |
| pickle_pure_python   | 310 us                                                 | 325 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                               |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                               |
| django_template | 35.2 ms                                                | 36.4 ms: 1.03x slower                                               |
| genshi_text     | 23.5 ms                                                | 24.5 ms: 1.04x slower                                               |
| genshi_xml      | 50.9 ms                                                | 58.4 ms: 1.15x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.4 us: 1.33x faster                                               |
| deepcopy                   | 358 us                                                 | 270 us: 1.33x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                |
| richards                   | 48.7 ms                                                | 39.9 ms: 1.22x faster                                               |
| richards_super             | 54.9 ms                                                | 45.7 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.20 us                                                | 2.72 us: 1.18x faster                                               |
| scimark_fft                | 364 ms                                                 | 319 ms: 1.14x faster                                                |
| telco                      | 8.54 ms                                                | 7.63 ms: 1.12x faster                                               |
| crypto_pyaes               | 75.3 ms                                                | 68.3 ms: 1.10x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 79.3 ms: 1.09x faster                                               |
| json                       | 5.36 ms                                                | 4.91 ms: 1.09x faster                                               |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                               |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.62 ms: 1.09x faster                                               |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                               |
| tomli_loads                | 2.14 sec                                               | 1.97 sec: 1.08x faster                                              |
| xml_etree_process          | 60.6 ms                                                | 56.2 ms: 1.08x faster                                               |
| go                         | 144 ms                                                 | 134 ms: 1.07x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                                |
| bpe_tokeniser              | 4.75 sec                                               | 4.46 sec: 1.06x faster                                              |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                               |
| nbody                      | 87.0 ms                                                | 81.9 ms: 1.06x faster                                               |
| async_tree_none            | 351 ms                                                 | 333 ms: 1.05x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                              |
| fannkuch                   | 404 ms                                                 | 387 ms: 1.04x faster                                                |
| logging_format             | 6.40 us                                                | 6.14 us: 1.04x faster                                               |
| float                      | 79.2 ms                                                | 76.0 ms: 1.04x faster                                               |
| logging_silent             | 102 ns                                                 | 97.9 ns: 1.04x faster                                               |
| scimark_monte_carlo        | 67.4 ms                                                | 65.1 ms: 1.04x faster                                               |
| pyflate                    | 471 ms                                                 | 459 ms: 1.03x faster                                                |
| scimark_sor                | 124 ms                                                 | 121 ms: 1.02x faster                                                |
| thrift                     | 809 us                                                 | 790 us: 1.02x faster                                                |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                                |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                               |
| connected_components       | 444 ms                                                 | 438 ms: 1.01x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                               |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                |
| regex_effbot               | 3.73 ms                                                | 3.72 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                |
| mdp                        | 2.72 sec                                               | 2.73 sec: 1.00x slower                                              |
| shortest_path              | 481 ms                                                 | 483 ms: 1.01x slower                                                |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                              |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                |
| coverage                   | 84.0 ms                                                | 85.1 ms: 1.01x slower                                               |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                               |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 136 ms: 1.02x slower                                                |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                               |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                               |
| html5lib                   | 64.2 ms                                                | 65.6 ms: 1.02x slower                                               |
| async_tree_io              | 842 ms                                                 | 862 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 559 ms: 1.02x slower                                                |
| regex_compile              | 132 ms                                                 | 135 ms: 1.02x slower                                                |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                               |
| typing_runtime_protocols   | 165 us                                                 | 169 us: 1.03x slower                                                |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.03x slower                                                |
| gc_traversal               | 4.37 ms                                                | 4.52 ms: 1.03x slower                                               |
| django_template            | 35.2 ms                                                | 36.4 ms: 1.03x slower                                               |
| raytrace                   | 267 ms                                                 | 277 ms: 1.04x slower                                                |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.7 ms: 1.04x slower                                               |
| async_generators           | 436 ms                                                 | 452 ms: 1.04x slower                                                |
| json_dumps                 | 10.6 ms                                                | 10.9 ms: 1.04x slower                                               |
| sqlglot_normalize          | 108 ms                                                 | 112 ms: 1.04x slower                                                |
| chaos                      | 58.1 ms                                                | 60.5 ms: 1.04x slower                                               |
| sqlglot_transpile          | 1.58 ms                                                | 1.65 ms: 1.04x slower                                               |
| genshi_text                | 23.5 ms                                                | 24.5 ms: 1.04x slower                                               |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                               |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                               |
| pickle_pure_python         | 310 us                                                 | 325 us: 1.05x slower                                                |
| dulwich_log                | 64.3 ms                                                | 67.4 ms: 1.05x slower                                               |
| sqlglot_optimize           | 53.7 ms                                                | 56.4 ms: 1.05x slower                                               |
| bench_thread_pool          | 822 us                                                 | 877 us: 1.07x slower                                                |
| sympy_str                  | 275 ms                                                 | 299 ms: 1.09x slower                                                |
| sympy_expand               | 463 ms                                                 | 504 ms: 1.09x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 21.9 ms: 1.10x slower                                               |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                               |
| sphinx                     | 1.03 sec                                               | 1.15 sec: 1.12x slower                                              |
| pylint                     | 313 ms                                                 | 349 ms: 1.12x slower                                                |
| sympy_sum                  | 150 ms                                                 | 168 ms: 1.12x slower                                                |
| nqueens                    | 78.4 ms                                                | 87.7 ms: 1.12x slower                                               |
| docutils                   | 2.59 sec                                               | 2.91 sec: 1.12x slower                                              |
| async_tree_io_tg           | 857 ms                                                 | 964 ms: 1.13x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 58.4 ms: 1.15x slower                                               |
| hexiom                     | 6.16 ms                                                | 7.13 ms: 1.16x slower                                               |
| generators                 | 29.0 ms                                                | 35.8 ms: 1.24x slower                                               |
| k_core                     | 2.35 sec                                               | 3.65 sec: 1.55x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 78.8 ms: 3.29x slower                                               |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (5): async_tree_none_tg, regex_dna, async_tree_cpu_io_mixed, 2to3, pprint_safe_repr
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241112-3.14.0a1+-f863657-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657.json: sqlite_synth

- Geometric mean (including insignificant results): 1.000x faster
# HPT report

- Reliability score: 89.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x