# Results vs. 3.13.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-amd64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.033x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 230 ms: 1.04x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 213 ms: 1.06x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 264 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 571 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.3 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 57.0 ms: 1.14x slower                                                      |
| nbody          | 68.4 ms                                                     | 89.2 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.6 ms: 1.37x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.64 ms: 1.04x slower                                                      |
| regex_dna      | 115 ms                                                      | 124 ms: 1.08x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 91.2 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.28 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.8 ms: 1.06x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 59.5 ms: 1.10x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 41.9 ms: 1.13x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 217 us: 1.14x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.65 sec: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                      |
| django_template | 22.4 ms                                                     | 25.0 ms: 1.12x slower                                                      |
| mako            | 6.35 ms                                                     | 7.17 ms: 1.13x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 522 us: 16.84x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 913 us: 1.38x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.6 ms: 1.37x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.57 ms: 1.25x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 69.2 ms: 1.25x faster                                                      |
| deepcopy                   | 226 us                                                      | 192 us: 1.18x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 21.3 us: 1.09x faster                                                      |
| async_tree_none            | 226 ms                                                      | 213 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.95 us: 1.06x faster                                                      |
| json                       | 3.19 ms                                                     | 3.02 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 264 ms: 1.04x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| go                         | 87.0 ms                                                     | 87.6 ms: 1.01x slower                                                      |
| tornado_http               | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.64 ms: 1.04x slower                                                      |
| 2to3                       | 221 ms                                                      | 230 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 110 us: 1.04x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 91.1 ms: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.28 ms: 1.06x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.34 us: 1.06x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.8 ms: 1.06x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 43.5 ms: 1.07x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 78.3 ms: 1.07x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                       |
| sympy_expand               | 291 ms                                                      | 311 ms: 1.07x slower                                                       |
| telco                      | 4.79 ms                                                     | 5.14 ms: 1.07x slower                                                      |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.08x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                     |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.77 us: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| genshi_text                | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                      |
| coverage                   | 45.6 ms                                                     | 49.4 ms: 1.08x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 49.6 ms: 1.09x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 59.5 ms: 1.10x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 571 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| spectral_norm              | 62.8 ms                                                     | 69.9 ms: 1.11x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 195 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                       |
| django_template            | 22.4 ms                                                     | 25.0 ms: 1.12x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.3 ms: 1.12x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 37.0 ms: 1.13x slower                                                      |
| mako                       | 6.35 ms                                                     | 7.17 ms: 1.13x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 41.9 ms: 1.13x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 91.2 ms: 1.13x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 562 ms: 1.14x slower                                                       |
| float                      | 49.9 ms                                                     | 57.0 ms: 1.14x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 217 us: 1.14x slower                                                       |
| chaos                      | 38.5 ms                                                     | 44.2 ms: 1.15x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.15 sec: 1.15x slower                                                     |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 65.8 ms: 1.16x slower                                                      |
| pyflate                    | 283 ms                                                      | 329 ms: 1.16x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.53 ms: 1.16x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.89 ms: 1.18x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 64.4 ns: 1.18x slower                                                      |
| raytrace                   | 160 ms                                                      | 189 ms: 1.18x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.65 sec: 1.18x slower                                                     |
| sqlglot_parse              | 771 us                                                      | 913 us: 1.18x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.19x slower                                                      |
| comprehensions             | 10.3 us                                                     | 12.2 us: 1.19x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.6 ms: 1.19x slower                                                      |
| richards_super             | 30.9 ms                                                     | 36.9 ms: 1.19x slower                                                      |
| fannkuch                   | 253 ms                                                      | 303 ms: 1.20x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.30 ms: 1.20x slower                                                      |
| pycparser                  | 683 ms                                                      | 824 ms: 1.21x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 64.6 ms: 1.22x slower                                                      |
| scimark_fft                | 172 ms                                                      | 214 ms: 1.24x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 95.7 ms: 1.26x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 52.4 ms: 1.28x slower                                                      |
| nbody                      | 68.4 ms                                                     | 89.2 ms: 1.30x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (4): bench_thread_pool, async_tree_none_tg, python_startup_no_site, genshi_xml
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.033x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown