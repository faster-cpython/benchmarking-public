# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-x86_64
- commit hash: 2e7a174
- commit date: 2024-11-13
- overall geometric mean: 1.011x slower
- HPT reliability: 73.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 297 ms: 1.01x slower                                                       |
| docutils       | 2.81 sec                                                     | 3.14 sec: 1.12x slower                                                     |
| html5lib       | 72.9 ms                                                      | 72.0 ms: 1.01x faster                                                      |
| sphinx         | 1.11 sec                                                     | 1.24 sec: 1.11x slower                                                     |
| Geometric mean | (ref)                                                        | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 376 ms: 1.22x faster                                                       |
| async_tree_none            | 370 ms                                                       | 340 ms: 1.09x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 416 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 324 ms: 1.06x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 584 ms: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                      |
| async_tree_io              | 832 ms                                                       | 857 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 823 ms                                                       | 871 ms: 1.06x slower                                                       |
| async_generators           | 364 ms                                                       | 482 ms: 1.33x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.7 ms: 1.05x faster                                                      |
| float          | 81.6 ms                                                      | 80.1 ms: 1.02x faster                                                      |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 142 ms: 1.01x faster                                                       |
| regex_effbot   | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                      |
| regex_v8       | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                                      |
| regex_dna      | 238 ms                                                       | 249 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.14 sec: 1.14x faster                                                     |
| unpickle_pure_python | 216 us                                                       | 197 us: 1.10x faster                                                       |
| xml_etree_process    | 60.7 ms                                                      | 59.1 ms: 1.03x faster                                                      |
| xml_etree_generate   | 85.2 ms                                                      | 83.1 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.02x slower                                                      |
| json_dumps           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                      |
| pickle_pure_python   | 322 us                                                       | 334 us: 1.04x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 152 ms: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                      |
| python_startup         | 15.6 ms                                                      | 15.9 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.49 ms: 1.09x faster                                                      |
| genshi_xml      | 58.0 ms                                                      | 60.7 ms: 1.05x slower                                                      |
| django_template | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 30.2 us: 1.29x faster                                                      |
| richards_super             | 60.2 ms                                                      | 48.7 ms: 1.24x faster                                                      |
| deepcopy                   | 388 us                                                       | 318 us: 1.22x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 376 ms: 1.22x faster                                                       |
| richards                   | 52.5 ms                                                      | 43.2 ms: 1.21x faster                                                      |
| telco                      | 8.77 ms                                                      | 7.62 ms: 1.15x faster                                                      |
| tomli_loads                | 2.43 sec                                                     | 2.14 sec: 1.14x faster                                                     |
| scimark_sor                | 125 ms                                                       | 111 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 3.13 us: 1.12x faster                                                      |
| unpickle_pure_python       | 216 us                                                       | 197 us: 1.10x faster                                                       |
| connected_components       | 443 ms                                                       | 404 ms: 1.09x faster                                                       |
| go                         | 167 ms                                                       | 153 ms: 1.09x faster                                                       |
| async_tree_none            | 370 ms                                                       | 340 ms: 1.09x faster                                                       |
| mako                       | 10.3 ms                                                      | 9.49 ms: 1.09x faster                                                      |
| json                       | 5.62 ms                                                      | 5.17 ms: 1.09x faster                                                      |
| shortest_path              | 477 ms                                                       | 442 ms: 1.08x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 416 ms: 1.07x faster                                                       |
| pyflate                    | 493 ms                                                       | 463 ms: 1.06x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 16.5 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 342 ms                                                       | 324 ms: 1.06x faster                                                       |
| coverage                   | 84.5 ms                                                      | 80.4 ms: 1.05x faster                                                      |
| nbody                      | 92.1 ms                                                      | 87.7 ms: 1.05x faster                                                      |
| pycparser                  | 1.28 sec                                                     | 1.24 sec: 1.04x faster                                                     |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                     |
| deltablue                  | 3.38 ms                                                      | 3.28 ms: 1.03x faster                                                      |
| bpe_tokeniser              | 5.09 sec                                                     | 4.95 sec: 1.03x faster                                                     |
| xml_etree_process          | 60.7 ms                                                      | 59.1 ms: 1.03x faster                                                      |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 83.1 ms: 1.03x faster                                                      |
| logging_silent             | 97.5 ns                                                      | 95.1 ns: 1.03x faster                                                      |
| pprint_safe_repr           | 835 ms                                                       | 817 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 584 ms: 1.02x faster                                                       |
| float                      | 81.6 ms                                                      | 80.1 ms: 1.02x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                      |
| html5lib                   | 72.9 ms                                                      | 72.0 ms: 1.01x faster                                                      |
| sqlalchemy_declarative     | 148 ms                                                       | 147 ms: 1.01x faster                                                       |
| regex_compile              | 143 ms                                                       | 142 ms: 1.01x faster                                                       |
| scimark_lu                 | 97.4 ms                                                      | 97.0 ms: 1.00x faster                                                      |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 98.5 ms: 1.01x slower                                                      |
| python_startup_no_site     | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                      |
| regex_effbot               | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                      |
| 2to3                       | 293 ms                                                       | 297 ms: 1.01x slower                                                       |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.01x slower                                                       |
| python_startup             | 15.6 ms                                                      | 15.9 ms: 1.02x slower                                                      |
| mdp                        | 2.53 sec                                                     | 2.58 sec: 1.02x slower                                                     |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                                      |
| fannkuch                   | 384 ms                                                       | 394 ms: 1.03x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 176 us                                                       | 180 us: 1.03x slower                                                       |
| async_tree_io              | 832 ms                                                       | 857 ms: 1.03x slower                                                       |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.7 ms: 1.03x slower                                                      |
| scimark_fft                | 298 ms                                                       | 308 ms: 1.03x slower                                                       |
| json_dumps                 | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                      |
| dulwich_log                | 65.5 ms                                                      | 68.0 ms: 1.04x slower                                                      |
| pickle_pure_python         | 322 us                                                       | 334 us: 1.04x slower                                                       |
| bench_thread_pool          | 929 us                                                       | 966 us: 1.04x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.53 us: 1.04x slower                                                      |
| genshi_xml                 | 58.0 ms                                                      | 60.7 ms: 1.05x slower                                                      |
| logging_format             | 6.95 us                                                      | 7.27 us: 1.05x slower                                                      |
| regex_dna                  | 238 ms                                                       | 249 ms: 1.05x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 152 ms: 1.05x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.0 ms: 1.06x slower                                                      |
| async_tree_io_tg           | 823 ms                                                       | 871 ms: 1.06x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 163 ms: 1.06x slower                                                       |
| sympy_integrate            | 23.4 ms                                                      | 24.9 ms: 1.07x slower                                                      |
| sympy_expand               | 506 ms                                                       | 545 ms: 1.08x slower                                                       |
| sympy_str                  | 297 ms                                                       | 319 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 58.7 ms                                                      | 64.0 ms: 1.09x slower                                                      |
| pylint                     | 345 ms                                                       | 377 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 130 ms: 1.09x slower                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 2.90 ms: 1.09x slower                                                      |
| django_template            | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                      |
| chaos                      | 60.6 ms                                                      | 66.7 ms: 1.10x slower                                                      |
| sqlglot_parse              | 1.37 ms                                                      | 1.51 ms: 1.10x slower                                                      |
| nqueens                    | 92.3 ms                                                      | 102 ms: 1.11x slower                                                       |
| sphinx                     | 1.11 sec                                                     | 1.24 sec: 1.11x slower                                                     |
| docutils                   | 2.81 sec                                                     | 3.14 sec: 1.12x slower                                                     |
| hexiom                     | 6.47 ms                                                      | 7.27 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.78 ms: 1.13x slower                                                      |
| comprehensions             | 17.3 us                                                      | 19.9 us: 1.15x slower                                                      |
| generators                 | 33.9 ms                                                      | 39.9 ms: 1.18x slower                                                      |
| raytrace                   | 267 ms                                                       | 327 ms: 1.22x slower                                                       |
| async_generators           | 364 ms                                                       | 482 ms: 1.33x slower                                                       |
| gc_traversal               | 4.48 ms                                                      | 6.10 ms: 1.36x slower                                                      |
| k_core                     | 2.18 sec                                                     | 3.04 sec: 1.40x slower                                                     |
| bench_mp_pool              | 4.82 ms                                                      | 1.60 sec: 331.76x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                               |

Benchmark hidden because not significant (3): thrift, crypto_pyaes, genshi_text
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241113-3.14.0a1+-2e7a174-JIT/bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174.json: sqlite_synth

- Geometric mean (including insignificant results): 1.011x slower
# HPT report

- Reliability score: 73.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x