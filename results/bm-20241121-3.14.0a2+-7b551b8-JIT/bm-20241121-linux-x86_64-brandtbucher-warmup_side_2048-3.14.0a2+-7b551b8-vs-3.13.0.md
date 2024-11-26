# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_2048
- machine: linux-x86_64
- commit hash: 7b551b8
- commit date: 2024-11-21
- overall geometric mean: 1.015x faster
- HPT reliability: 69.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 261 ms: 1.02x faster                                                     |
| docutils       | 2.59 sec                                               | 2.79 sec: 1.08x slower                                                   |
| html5lib       | 64.2 ms                                                | 66.9 ms: 1.04x slower                                                    |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 399 ms: 1.16x faster                                                     |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.07x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 565 ms: 1.02x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 566 ms: 1.04x slower                                                     |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 921 ms: 1.08x slower                                                     |
| async_tree_io              | 842 ms                                                 | 914 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.3 ms: 1.06x faster                                                    |
| float          | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                    |
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.50 ms: 1.06x faster                                                    |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| regex_v8       | 26.2 ms                                                | 26.0 ms: 1.01x faster                                                    |
| regex_dna      | 218 ms                                                 | 226 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 193 us: 1.12x faster                                                     |
| xml_etree_generate   | 86.7 ms                                                | 78.5 ms: 1.10x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 55.3 ms: 1.10x faster                                                    |
| tomli_loads          | 2.14 sec                                               | 1.97 sec: 1.09x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.06x faster                                                     |
| json_loads           | 27.2 us                                                | 26.3 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                                     |
| pickle_pure_python   | 310 us                                                 | 316 us: 1.02x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                    |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.93 ms: 1.12x faster                                                    |
| django_template | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                    |
| genshi_text     | 23.5 ms                                                | 24.6 ms: 1.05x slower                                                    |
| genshi_xml      | 50.9 ms                                                | 59.1 ms: 1.16x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                                     |
| deepcopy_memo              | 39.1 us                                                | 29.3 us: 1.33x faster                                                    |
| richards                   | 48.7 ms                                                | 39.4 ms: 1.24x faster                                                    |
| richards_super             | 54.9 ms                                                | 45.8 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 3.20 us                                                | 2.71 us: 1.18x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 399 ms: 1.16x faster                                                     |
| scimark_fft                | 364 ms                                                 | 318 ms: 1.15x faster                                                     |
| pylint                     | 313 ms                                                 | 275 ms: 1.14x faster                                                     |
| unpickle_pure_python       | 216 us                                                 | 193 us: 1.12x faster                                                     |
| telco                      | 8.54 ms                                                | 7.63 ms: 1.12x faster                                                    |
| mako                       | 11.1 ms                                                | 9.93 ms: 1.12x faster                                                    |
| json                       | 5.36 ms                                                | 4.80 ms: 1.12x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 68.1 ms: 1.11x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 78.5 ms: 1.10x faster                                                    |
| go                         | 144 ms                                                 | 131 ms: 1.10x faster                                                     |
| xml_etree_process          | 60.6 ms                                                | 55.3 ms: 1.10x faster                                                    |
| tomli_loads                | 2.14 sec                                               | 1.97 sec: 1.09x faster                                                   |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.67 ms: 1.08x faster                                                    |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.07x faster                                                     |
| pyflate                    | 471 ms                                                 | 439 ms: 1.07x faster                                                     |
| regex_effbot               | 3.73 ms                                                | 3.50 ms: 1.06x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                                     |
| nbody                      | 87.0 ms                                                | 82.3 ms: 1.06x faster                                                    |
| django_template            | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                   |
| fannkuch                   | 404 ms                                                 | 385 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.52 sec: 1.05x faster                                                   |
| logging_format             | 6.40 us                                                | 6.18 us: 1.04x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.3 us: 1.03x faster                                                    |
| meteor_contest             | 109 ms                                                 | 105 ms: 1.03x faster                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 65.3 ms: 1.03x faster                                                    |
| thrift                     | 809 us                                                 | 785 us: 1.03x faster                                                     |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                     |
| connected_components       | 444 ms                                                 | 431 ms: 1.03x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.03x faster                                                     |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| 2to3                       | 267 ms                                                 | 261 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 565 ms: 1.02x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                    |
| float                      | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                    |
| logging_silent             | 102 ns                                                 | 100 ns: 1.01x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 26.0 ms: 1.01x faster                                                    |
| shortest_path              | 481 ms                                                 | 478 ms: 1.01x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                                   |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                    |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                    |
| pickle_pure_python         | 310 us                                                 | 316 us: 1.02x slower                                                     |
| chaos                      | 58.1 ms                                                | 59.3 ms: 1.02x slower                                                    |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                     |
| mdp                        | 2.72 sec                                               | 2.78 sec: 1.02x slower                                                   |
| gc_traversal               | 4.37 ms                                                | 4.47 ms: 1.02x slower                                                    |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 165 us                                                 | 169 us: 1.02x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                    |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                     |
| sympy_str                  | 275 ms                                                 | 283 ms: 1.03x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                                    |
| regex_dna                  | 218 ms                                                 | 226 ms: 1.03x slower                                                     |
| sympy_expand               | 463 ms                                                 | 480 ms: 1.03x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 55.7 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 566 ms: 1.04x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 20.7 ms: 1.04x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                     |
| html5lib                   | 64.2 ms                                                | 66.9 ms: 1.04x slower                                                    |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                     |
| genshi_text                | 23.5 ms                                                | 24.6 ms: 1.05x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.4 ms: 1.05x slower                                                    |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                    |
| bench_thread_pool          | 822 us                                                 | 873 us: 1.06x slower                                                     |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                   |
| raytrace                   | 267 ms                                                 | 285 ms: 1.07x slower                                                     |
| comprehensions             | 16.5 us                                                | 17.7 us: 1.07x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 921 ms: 1.08x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.79 sec: 1.08x slower                                                   |
| async_tree_io              | 842 ms                                                 | 914 ms: 1.09x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.64 ms: 1.10x slower                                                    |
| nqueens                    | 78.4 ms                                                | 87.9 ms: 1.12x slower                                                    |
| hexiom                     | 6.16 ms                                                | 7.11 ms: 1.15x slower                                                    |
| genshi_xml                 | 50.9 ms                                                | 59.1 ms: 1.16x slower                                                    |
| k_core                     | 2.35 sec                                               | 2.90 sec: 1.23x slower                                                   |
| generators                 | 29.0 ms                                                | 37.1 ms: 1.28x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (5): async_tree_none_tg, spectral_norm, deltablue, pprint_safe_repr, coverage
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241121-3.14.0a2+-7b551b8-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.015x faster
# HPT report

- Reliability score: 69.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x