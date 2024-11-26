# Results vs. base

- fork: brandtbucher
- ref: optimize_off_all
- machine: linux-x86_64
- commit hash: dff2fa8
- commit date: 2024-11-17
- overall geometric mean: 1.063x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                 | 303 ms: 1.08x slower                                                     |
| docutils       | 2.93 sec                                                               | 3.27 sec: 1.12x slower                                                   |
| html5lib       | 66.3 ms                                                                | 68.5 ms: 1.03x slower                                                    |
| sphinx         | 1.17 sec                                                               | 1.21 sec: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines                 | 22.8 ms                                                                | 22.4 ms: 1.02x faster                                                    |
| asyncio_websockets         | 552 ms                                                                 | 555 ms: 1.00x slower                                                     |
| async_tree_none            | 337 ms                                                                 | 343 ms: 1.02x slower                                                     |
| async_tree_memoization_tg  | 382 ms                                                                 | 389 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed    | 580 ms                                                                 | 592 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 574 ms: 1.02x slower                                                     |
| async_generators           | 451 ms                                                                 | 462 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.5 ms                                                                | 81.7 ms: 1.07x slower                                                    |
| nbody          | 82.4 ms                                                                | 102 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.10x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.66 ms                                                                | 3.62 ms: 1.01x faster                                                    |
| regex_v8       | 25.2 ms                                                                | 25.1 ms: 1.00x faster                                                    |
| regex_dna      | 211 ms                                                                 | 219 ms: 1.04x slower                                                     |
| regex_compile  | 142 ms                                                                 | 162 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 26.5 us                                                                | 26.2 us: 1.01x faster                                                    |
| json_dumps           | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                    |
| xml_etree_parse      | 147 ms                                                                 | 150 ms: 1.02x slower                                                     |
| xml_etree_iterparse  | 101 ms                                                                 | 104 ms: 1.02x slower                                                     |
| unpickle_pure_python | 217 us                                                                 | 229 us: 1.05x slower                                                     |
| tomli_loads          | 1.94 sec                                                               | 2.08 sec: 1.07x slower                                                   |
| xml_etree_generate   | 79.5 ms                                                                | 86.3 ms: 1.09x slower                                                    |
| pickle_pure_python   | 322 us                                                                 | 350 us: 1.09x slower                                                     |
| xml_etree_process    | 55.6 ms                                                                | 62.2 ms: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.05x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                                | 7.08 ms: 1.01x faster                                                    |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 33.8 ms                                                                | 35.8 ms: 1.06x slower                                                    |
| genshi_text     | 25.2 ms                                                                | 27.3 ms: 1.08x slower                                                    |
| mako            | 10.1 ms                                                                | 11.0 ms: 1.09x slower                                                    |
| genshi_xml      | 57.8 ms                                                                | 67.0 ms: 1.16x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.10x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 4.81 ms                                                                | 4.53 ms: 1.06x faster                                                    |
| coroutines                 | 22.8 ms                                                                | 22.4 ms: 1.02x faster                                                    |
| regex_effbot               | 3.66 ms                                                                | 3.62 ms: 1.01x faster                                                    |
| python_startup_no_site     | 7.16 ms                                                                | 7.08 ms: 1.01x faster                                                    |
| json_loads                 | 26.5 us                                                                | 26.2 us: 1.01x faster                                                    |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                                    |
| create_gc_cycles           | 2.70 ms                                                                | 2.68 ms: 1.01x faster                                                    |
| regex_v8                   | 25.2 ms                                                                | 25.1 ms: 1.00x faster                                                    |
| asyncio_websockets         | 552 ms                                                                 | 555 ms: 1.00x slower                                                     |
| thrift                     | 787 us                                                                 | 794 us: 1.01x slower                                                     |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                    |
| coverage                   | 83.5 ms                                                                | 84.4 ms: 1.01x slower                                                    |
| k_core                     | 3.62 sec                                                               | 3.66 sec: 1.01x slower                                                   |
| json                       | 4.89 ms                                                                | 4.95 ms: 1.01x slower                                                    |
| sqlite_synth               | 2.79 us                                                                | 2.83 us: 1.01x slower                                                    |
| sqlalchemy_imperative      | 17.8 ms                                                                | 18.1 ms: 1.02x slower                                                    |
| json_dumps                 | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                    |
| async_tree_none            | 337 ms                                                                 | 343 ms: 1.02x slower                                                     |
| async_tree_memoization_tg  | 382 ms                                                                 | 389 ms: 1.02x slower                                                     |
| bench_thread_pool          | 899 us                                                                 | 916 us: 1.02x slower                                                     |
| mdp                        | 2.59 sec                                                               | 2.64 sec: 1.02x slower                                                   |
| shortest_path              | 482 ms                                                                 | 491 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed    | 580 ms                                                                 | 592 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 574 ms: 1.02x slower                                                     |
| xml_etree_parse            | 147 ms                                                                 | 150 ms: 1.02x slower                                                     |
| xml_etree_iterparse        | 101 ms                                                                 | 104 ms: 1.02x slower                                                     |
| connected_components       | 438 ms                                                                 | 448 ms: 1.02x slower                                                     |
| async_generators           | 451 ms                                                                 | 462 ms: 1.03x slower                                                     |
| logging_format             | 6.17 us                                                                | 6.34 us: 1.03x slower                                                    |
| html5lib                   | 66.3 ms                                                                | 68.5 ms: 1.03x slower                                                    |
| sphinx                     | 1.17 sec                                                               | 1.21 sec: 1.03x slower                                                   |
| meteor_contest             | 108 ms                                                                 | 112 ms: 1.03x slower                                                     |
| regex_dna                  | 211 ms                                                                 | 219 ms: 1.04x slower                                                     |
| logging_simple             | 5.60 us                                                                | 5.81 us: 1.04x slower                                                    |
| sqlalchemy_declarative     | 147 ms                                                                 | 153 ms: 1.04x slower                                                     |
| telco                      | 7.50 ms                                                                | 7.83 ms: 1.04x slower                                                    |
| subparsers                 | 21.2 ms                                                                | 22.2 ms: 1.05x slower                                                    |
| sympy_expand               | 510 ms                                                                 | 535 ms: 1.05x slower                                                     |
| dulwich_log                | 67.5 ms                                                                | 71.1 ms: 1.05x slower                                                    |
| sympy_sum                  | 178 ms                                                                 | 187 ms: 1.05x slower                                                     |
| unpickle_pure_python       | 217 us                                                                 | 229 us: 1.05x slower                                                     |
| sympy_str                  | 306 ms                                                                 | 325 ms: 1.06x slower                                                     |
| django_template            | 33.8 ms                                                                | 35.8 ms: 1.06x slower                                                    |
| nqueens                    | 89.6 ms                                                                | 95.0 ms: 1.06x slower                                                    |
| crypto_pyaes               | 69.1 ms                                                                | 73.5 ms: 1.06x slower                                                    |
| sympy_integrate            | 23.7 ms                                                                | 25.3 ms: 1.07x slower                                                    |
| float                      | 76.5 ms                                                                | 81.7 ms: 1.07x slower                                                    |
| tomli_loads                | 1.94 sec                                                               | 2.08 sec: 1.07x slower                                                   |
| typing_runtime_protocols   | 166 us                                                                 | 179 us: 1.08x slower                                                     |
| bpe_tokeniser              | 4.46 sec                                                               | 4.80 sec: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 4.54 ms                                                                | 4.88 ms: 1.08x slower                                                    |
| raytrace                   | 285 ms                                                                 | 307 ms: 1.08x slower                                                     |
| 2to3                       | 281 ms                                                                 | 303 ms: 1.08x slower                                                     |
| genshi_text                | 25.2 ms                                                                | 27.3 ms: 1.08x slower                                                    |
| scimark_fft                | 320 ms                                                                 | 347 ms: 1.08x slower                                                     |
| xml_etree_generate         | 79.5 ms                                                                | 86.3 ms: 1.09x slower                                                    |
| pickle_pure_python         | 322 us                                                                 | 350 us: 1.09x slower                                                     |
| sqlglot_normalize          | 115 ms                                                                 | 126 ms: 1.09x slower                                                     |
| mako                       | 10.1 ms                                                                | 11.0 ms: 1.09x slower                                                    |
| sqlglot_parse              | 1.33 ms                                                                | 1.46 ms: 1.09x slower                                                    |
| many_optionals             | 1.05 ms                                                                | 1.15 ms: 1.09x slower                                                    |
| deltablue                  | 3.31 ms                                                                | 3.63 ms: 1.10x slower                                                    |
| fannkuch                   | 391 ms                                                                 | 430 ms: 1.10x slower                                                     |
| sqlglot_optimize           | 60.2 ms                                                                | 66.6 ms: 1.11x slower                                                    |
| sqlglot_transpile          | 1.70 ms                                                                | 1.88 ms: 1.11x slower                                                    |
| pyflate                    | 457 ms                                                                 | 507 ms: 1.11x slower                                                     |
| pycparser                  | 1.15 sec                                                               | 1.28 sec: 1.11x slower                                                   |
| scimark_lu                 | 115 ms                                                                 | 128 ms: 1.12x slower                                                     |
| deepcopy_reduce            | 2.70 us                                                                | 3.01 us: 1.12x slower                                                    |
| docutils                   | 2.93 sec                                                               | 3.27 sec: 1.12x slower                                                   |
| xml_etree_process          | 55.6 ms                                                                | 62.2 ms: 1.12x slower                                                    |
| comprehensions             | 17.6 us                                                                | 19.8 us: 1.12x slower                                                    |
| deepcopy                   | 269 us                                                                 | 303 us: 1.12x slower                                                     |
| spectral_norm              | 114 ms                                                                 | 128 ms: 1.13x slower                                                     |
| generators                 | 36.0 ms                                                                | 40.9 ms: 1.13x slower                                                    |
| regex_compile              | 142 ms                                                                 | 162 ms: 1.14x slower                                                     |
| chaos                      | 59.1 ms                                                                | 67.6 ms: 1.14x slower                                                    |
| go                         | 133 ms                                                                 | 152 ms: 1.15x slower                                                     |
| scimark_monte_carlo        | 64.0 ms                                                                | 73.6 ms: 1.15x slower                                                    |
| scimark_sor                | 119 ms                                                                 | 138 ms: 1.16x slower                                                     |
| genshi_xml                 | 57.8 ms                                                                | 67.0 ms: 1.16x slower                                                    |
| deepcopy_memo              | 29.4 us                                                                | 34.5 us: 1.17x slower                                                    |
| logging_silent             | 98.9 ns                                                                | 116 ns: 1.18x slower                                                     |
| hexiom                     | 7.15 ms                                                                | 8.50 ms: 1.19x slower                                                    |
| nbody                      | 82.4 ms                                                                | 102 ms: 1.24x slower                                                     |
| richards                   | 40.0 ms                                                                | 50.2 ms: 1.26x slower                                                    |
| richards_super             | 46.0 ms                                                                | 58.7 ms: 1.28x slower                                                    |
| pprint_safe_repr           | 741 ms                                                                 | 995 ms: 1.34x slower                                                     |
| pprint_pformat             | 1.52 sec                                                               | 2.14 sec: 1.41x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.07x slower                                                             |

Benchmark hidden because not significant (8): async_tree_io_tg, pidigits, bench_mp_pool, async_tree_none_tg, async_tree_io, djangocms, async_tree_memoization, pylint

- Geometric mean (including insignificant results): 1.063x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.02x