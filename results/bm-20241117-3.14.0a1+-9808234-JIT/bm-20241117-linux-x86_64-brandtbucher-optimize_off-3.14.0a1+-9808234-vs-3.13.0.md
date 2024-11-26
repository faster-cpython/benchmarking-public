# Results vs. 3.13.0

- fork: brandtbucher
- ref: optimize_off
- machine: linux-x86_64
- commit hash: 9808234
- commit date: 2024-11-17
- overall geometric mean: 1.013x slower
- HPT reliability: 96.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 283 ms: 1.06x slower                                                 |
| docutils       | 2.59 sec                                               | 3.13 sec: 1.21x slower                                               |
| html5lib       | 64.2 ms                                                | 68.6 ms: 1.07x slower                                                |
| sphinx         | 1.03 sec                                               | 1.18 sec: 1.14x slower                                               |
| Geometric mean | (ref)                                                  | 1.12x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                                 |
| async_tree_none            | 351 ms                                                 | 333 ms: 1.05x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 421 ms: 1.05x faster                                                 |
| async_tree_io              | 842 ms                                                 | 858 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 560 ms: 1.03x slower                                                 |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (4): coroutines, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                |
| float          | 79.2 ms                                                | 77.2 ms: 1.03x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                |
| regex_dna      | 218 ms                                                 | 215 ms: 1.01x faster                                                 |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.12x faster                                               |
| xml_etree_generate   | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                |
| xml_etree_process    | 60.6 ms                                                | 56.2 ms: 1.08x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                 |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.02x faster                                                |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                 |
| pickle_pure_python   | 310 us                                                 | 328 us: 1.06x slower                                                 |
| json_dumps           | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                |
| django_template | 35.2 ms                                                | 34.3 ms: 1.02x faster                                                |
| genshi_text     | 23.5 ms                                                | 24.8 ms: 1.05x slower                                                |
| genshi_xml      | 50.9 ms                                                | 60.8 ms: 1.19x slower                                                |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.5 us: 1.32x faster                                                |
| deepcopy                   | 358 us                                                 | 272 us: 1.32x faster                                                 |
| richards                   | 48.7 ms                                                | 39.7 ms: 1.23x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.18x faster                                                |
| telco                      | 8.54 ms                                                | 7.42 ms: 1.15x faster                                                |
| richards_super             | 54.9 ms                                                | 48.2 ms: 1.14x faster                                                |
| scimark_fft                | 364 ms                                                 | 325 ms: 1.12x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 1.92 sec: 1.12x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 69.1 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.64 ms: 1.09x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 56.2 ms: 1.08x faster                                                |
| mako                       | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                |
| json                       | 5.36 ms                                                | 5.03 ms: 1.07x faster                                                |
| go                         | 144 ms                                                 | 136 ms: 1.06x faster                                                 |
| bpe_tokeniser              | 4.75 sec                                               | 4.48 sec: 1.06x faster                                               |
| async_tree_none            | 351 ms                                                 | 333 ms: 1.05x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 421 ms: 1.05x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 64.6 ms: 1.04x faster                                                |
| regex_v8                   | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                |
| fannkuch                   | 404 ms                                                 | 390 ms: 1.04x faster                                                 |
| mdp                        | 2.72 sec                                               | 2.63 sec: 1.03x faster                                               |
| nbody                      | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                |
| pyflate                    | 471 ms                                                 | 458 ms: 1.03x faster                                                 |
| float                      | 79.2 ms                                                | 77.2 ms: 1.03x faster                                                |
| django_template            | 35.2 ms                                                | 34.3 ms: 1.02x faster                                                |
| logging_format             | 6.40 us                                                | 6.24 us: 1.02x faster                                                |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                                |
| thrift                     | 809 us                                                 | 795 us: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.02x faster                                                |
| regex_dna                  | 218 ms                                                 | 215 ms: 1.01x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.64 us: 1.01x faster                                                |
| connected_components       | 444 ms                                                 | 439 ms: 1.01x faster                                                 |
| scimark_sor                | 124 ms                                                 | 122 ms: 1.01x faster                                                 |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| coverage                   | 84.0 ms                                                | 84.7 ms: 1.01x slower                                                |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                 |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                |
| async_tree_io              | 842 ms                                                 | 858 ms: 1.02x slower                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.53 sec: 1.02x slower                                               |
| pprint_safe_repr           | 728 ms                                                 | 747 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 560 ms: 1.03x slower                                                 |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                |
| typing_runtime_protocols   | 165 us                                                 | 170 us: 1.03x slower                                                 |
| gc_traversal               | 4.37 ms                                                | 4.52 ms: 1.03x slower                                                |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.7 ms: 1.04x slower                                                |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                 |
| deltablue                  | 3.23 ms                                                | 3.39 ms: 1.05x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                |
| genshi_text                | 23.5 ms                                                | 24.8 ms: 1.05x slower                                                |
| pickle_pure_python         | 310 us                                                 | 328 us: 1.06x slower                                                 |
| spectral_norm              | 115 ms                                                 | 122 ms: 1.06x slower                                                 |
| 2to3                       | 267 ms                                                 | 283 ms: 1.06x slower                                                 |
| chaos                      | 58.1 ms                                                | 61.5 ms: 1.06x slower                                                |
| dulwich_log                | 64.3 ms                                                | 68.6 ms: 1.07x slower                                                |
| html5lib                   | 64.2 ms                                                | 68.6 ms: 1.07x slower                                                |
| json_dumps                 | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 116 ms: 1.08x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.8 us: 1.08x slower                                                |
| regex_compile              | 132 ms                                                 | 143 ms: 1.08x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.72 ms: 1.09x slower                                                |
| bench_thread_pool          | 822 us                                                 | 895 us: 1.09x slower                                                 |
| raytrace                   | 267 ms                                                 | 292 ms: 1.09x slower                                                 |
| sympy_expand               | 463 ms                                                 | 508 ms: 1.10x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 147 ms: 1.10x slower                                                 |
| create_gc_cycles           | 2.41 ms                                                | 2.68 ms: 1.11x slower                                                |
| sympy_str                  | 275 ms                                                 | 307 ms: 1.12x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 60.6 ms: 1.13x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.18 sec: 1.14x slower                                               |
| nqueens                    | 78.4 ms                                                | 90.7 ms: 1.16x slower                                                |
| hexiom                     | 6.16 ms                                                | 7.19 ms: 1.17x slower                                                |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                 |
| genshi_xml                 | 50.9 ms                                                | 60.8 ms: 1.19x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 23.8 ms: 1.20x slower                                                |
| docutils                   | 2.59 sec                                               | 3.13 sec: 1.21x slower                                               |
| pylint                     | 313 ms                                                 | 385 ms: 1.23x slower                                                 |
| generators                 | 29.0 ms                                                | 36.4 ms: 1.26x slower                                                |
| k_core                     | 2.35 sec                                               | 3.63 sec: 1.54x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 84.5 ms: 3.52x slower                                                |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                         |

Benchmark hidden because not significant (8): logging_silent, pycparser, coroutines, async_tree_cpu_io_mixed, asyncio_websockets, shortest_path, regex_effbot, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241117-3.14.0a1+-9808234-JIT/bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.013x slower
# HPT report

- Reliability score: 96.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x