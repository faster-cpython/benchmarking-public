# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: darwin-arm64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 173 ms: 1.08x slower                                       |
| chameleon      | 4.27 ms                                                    | 5.03 ms: 1.18x slower                                      |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                     |
| tornado_http   | 66.7 ms                                                    | 70.3 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                      | 1.09x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 467 ms                                                     | 530 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed_tg | 451 ms                                                     | 538 ms: 1.19x slower                                       |
| async_tree_io_tg           | 565 ms                                                     | 682 ms: 1.21x slower                                       |
| async_tree_none            | 209 ms                                                     | 261 ms: 1.25x slower                                       |
| async_tree_io              | 563 ms                                                     | 715 ms: 1.27x slower                                       |
| async_tree_memoization     | 260 ms                                                     | 337 ms: 1.30x slower                                       |
| async_tree_none_tg         | 198 ms                                                     | 267 ms: 1.35x slower                                       |
| async_tree_memoization_tg  | 240 ms                                                     | 335 ms: 1.40x slower                                       |
| Geometric mean             | (ref)                                                      | 1.26x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 284 ms: 1.01x slower                                       |
| float          | 48.6 ms                                                    | 68.9 ms: 1.42x slower                                      |
| nbody          | 59.6 ms                                                    | 86.4 ms: 1.45x slower                                      |
| Geometric mean | (ref)                                                      | 1.27x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 17.9 ms: 1.04x slower                                      |
| regex_dna      | 149 ms                                                     | 156 ms: 1.04x slower                                       |
| regex_effbot   | 2.58 ms                                                    | 2.77 ms: 1.07x slower                                      |
| regex_compile  | 68.5 ms                                                    | 82.6 ms: 1.20x slower                                      |
| Geometric mean | (ref)                                                      | 1.09x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                      |
| pickle               | 7.48 us                                                    | 7.44 us: 1.01x faster                                      |
| pickle_list          | 2.96 us                                                    | 2.97 us: 1.00x slower                                      |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                      |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                       |
| json_dumps           | 6.23 ms                                                    | 6.61 ms: 1.06x slower                                      |
| unpickle_list        | 2.88 us                                                    | 3.07 us: 1.06x slower                                      |
| pickle_pure_python   | 179 us                                                     | 196 us: 1.10x slower                                       |
| xml_etree_process    | 37.1 ms                                                    | 40.9 ms: 1.10x slower                                      |
| xml_etree_generate   | 52.7 ms                                                    | 58.8 ms: 1.12x slower                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 80.9 ms: 1.13x slower                                      |
| tomli_loads          | 1.47 sec                                                   | 1.68 sec: 1.15x slower                                     |
| unpickle_pure_python | 141 us                                                     | 165 us: 1.17x slower                                       |
| Geometric mean       | (ref)                                                      | 1.06x slower                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 12.8 ms: 1.19x faster                                      |
| python_startup_no_site | 12.3 ms                                                    | 11.4 ms: 1.08x faster                                      |
| Geometric mean         | (ref)                                                      | 1.13x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 6.99 ms                                                    | 9.85 ms: 1.41x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 897 us                                                     | 703 us: 1.28x faster                                       |
| python_startup             | 15.2 ms                                                    | 12.8 ms: 1.19x faster                                      |
| typing_runtime_protocols   | 87.6 us                                                    | 74.1 us: 1.18x faster                                      |
| python_startup_no_site     | 12.3 ms                                                    | 11.4 ms: 1.08x faster                                      |
| bench_mp_pool              | 47.2 ms                                                    | 45.1 ms: 1.05x faster                                      |
| gc_traversal               | 2.45 ms                                                    | 2.40 ms: 1.02x faster                                      |
| pickle_dict                | 18.3 us                                                    | 18.1 us: 1.01x faster                                      |
| pickle                     | 7.48 us                                                    | 7.44 us: 1.01x faster                                      |
| pickle_list                | 2.96 us                                                    | 2.97 us: 1.00x slower                                      |
| pidigits                   | 282 ms                                                     | 284 ms: 1.01x slower                                       |
| json_loads                 | 16.8 us                                                    | 17.0 us: 1.01x slower                                      |
| xml_etree_parse            | 106 ms                                                     | 107 ms: 1.01x slower                                       |
| asyncio_tcp_ssl            | 1.29 sec                                                   | 1.32 sec: 1.02x slower                                     |
| dask                       | 221 ms                                                     | 227 ms: 1.03x slower                                       |
| telco                      | 4.60 ms                                                    | 4.73 ms: 1.03x slower                                      |
| richards                   | 31.8 ms                                                    | 32.8 ms: 1.03x slower                                      |
| regex_v8                   | 17.3 ms                                                    | 17.9 ms: 1.04x slower                                      |
| json                       | 2.93 ms                                                    | 3.04 ms: 1.04x slower                                      |
| richards_super             | 35.2 ms                                                    | 36.6 ms: 1.04x slower                                      |
| docutils                   | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                     |
| regex_dna                  | 149 ms                                                     | 156 ms: 1.04x slower                                       |
| mdp                        | 1.53 sec                                                   | 1.62 sec: 1.05x slower                                     |
| tornado_http               | 66.7 ms                                                    | 70.3 ms: 1.05x slower                                      |
| sqlite_synth               | 1.55 us                                                    | 1.64 us: 1.06x slower                                      |
| async_generators           | 281 ms                                                     | 297 ms: 1.06x slower                                       |
| json_dumps                 | 6.23 ms                                                    | 6.61 ms: 1.06x slower                                      |
| unpickle_list              | 2.88 us                                                    | 3.07 us: 1.06x slower                                      |
| coverage                   | 45.0 ms                                                    | 47.9 ms: 1.07x slower                                      |
| regex_effbot               | 2.58 ms                                                    | 2.77 ms: 1.07x slower                                      |
| 2to3                       | 161 ms                                                     | 173 ms: 1.08x slower                                       |
| dulwich_log                | 27.6 ms                                                    | 30.1 ms: 1.09x slower                                      |
| sympy_expand               | 226 ms                                                     | 247 ms: 1.09x slower                                       |
| meteor_contest             | 70.3 ms                                                    | 76.8 ms: 1.09x slower                                      |
| pathlib                    | 23.3 ms                                                    | 25.5 ms: 1.09x slower                                      |
| pickle_pure_python         | 179 us                                                     | 196 us: 1.10x slower                                       |
| xml_etree_process          | 37.1 ms                                                    | 40.9 ms: 1.10x slower                                      |
| deepcopy_reduce            | 1.82 us                                                    | 2.01 us: 1.10x slower                                      |
| crypto_pyaes               | 49.5 ms                                                    | 54.7 ms: 1.11x slower                                      |
| sqlglot_parse              | 732 us                                                     | 811 us: 1.11x slower                                       |
| go                         | 101 ms                                                     | 112 ms: 1.11x slower                                       |
| pycparser                  | 632 ms                                                     | 704 ms: 1.11x slower                                       |
| sqlglot_transpile          | 891 us                                                     | 994 us: 1.12x slower                                       |
| sympy_integrate            | 10.3 ms                                                    | 11.6 ms: 1.12x slower                                      |
| xml_etree_generate         | 52.7 ms                                                    | 58.8 ms: 1.12x slower                                      |
| scimark_sor                | 94.9 ms                                                    | 106 ms: 1.12x slower                                       |
| deepcopy                   | 204 us                                                     | 229 us: 1.12x slower                                       |
| sympy_str                  | 131 ms                                                     | 149 ms: 1.13x slower                                       |
| xml_etree_iterparse        | 71.5 ms                                                    | 80.9 ms: 1.13x slower                                      |
| async_tree_cpu_io_mixed    | 467 ms                                                     | 530 ms: 1.13x slower                                       |
| tomli_loads                | 1.47 sec                                                   | 1.68 sec: 1.15x slower                                     |
| scimark_lu                 | 66.9 ms                                                    | 76.7 ms: 1.15x slower                                      |
| sympy_sum                  | 69.2 ms                                                    | 79.4 ms: 1.15x slower                                      |
| sqlglot_normalize          | 166 ms                                                     | 191 ms: 1.15x slower                                       |
| bench_thread_pool          | 447 us                                                     | 517 us: 1.16x slower                                       |
| pyflate                    | 321 ms                                                     | 373 ms: 1.16x slower                                       |
| sqlglot_optimize           | 30.9 ms                                                    | 36.0 ms: 1.16x slower                                      |
| unpickle_pure_python       | 141 us                                                     | 165 us: 1.17x slower                                       |
| logging_format             | 3.31 us                                                    | 3.88 us: 1.17x slower                                      |
| logging_simple             | 3.04 us                                                    | 3.58 us: 1.18x slower                                      |
| chameleon                  | 4.27 ms                                                    | 5.03 ms: 1.18x slower                                      |
| deepcopy_memo              | 22.6 us                                                    | 26.8 us: 1.19x slower                                      |
| coroutines                 | 15.8 ms                                                    | 18.9 ms: 1.19x slower                                      |
| async_tree_cpu_io_mixed_tg | 451 ms                                                     | 538 ms: 1.19x slower                                       |
| logging_silent             | 60.1 ns                                                    | 72.1 ns: 1.20x slower                                      |
| regex_compile              | 68.5 ms                                                    | 82.6 ms: 1.20x slower                                      |
| async_tree_io_tg           | 565 ms                                                     | 682 ms: 1.21x slower                                       |
| pprint_safe_repr           | 465 ms                                                     | 575 ms: 1.24x slower                                       |
| pprint_pformat             | 947 ms                                                     | 1.18 sec: 1.24x slower                                     |
| async_tree_none            | 209 ms                                                     | 261 ms: 1.25x slower                                       |
| generators                 | 22.9 ms                                                    | 28.7 ms: 1.25x slower                                      |
| raytrace                   | 147 ms                                                     | 186 ms: 1.27x slower                                       |
| async_tree_io              | 563 ms                                                     | 715 ms: 1.27x slower                                       |
| async_tree_memoization     | 260 ms                                                     | 337 ms: 1.30x slower                                       |
| nqueens                    | 52.2 ms                                                    | 68.4 ms: 1.31x slower                                      |
| fannkuch                   | 248 ms                                                     | 328 ms: 1.32x slower                                       |
| scimark_monte_carlo        | 42.5 ms                                                    | 57.0 ms: 1.34x slower                                      |
| async_tree_none_tg         | 198 ms                                                     | 267 ms: 1.35x slower                                       |
| chaos                      | 34.0 ms                                                    | 46.7 ms: 1.37x slower                                      |
| scimark_fft                | 181 ms                                                     | 249 ms: 1.38x slower                                       |
| mypy2                      | 379 ms                                                     | 530 ms: 1.40x slower                                       |
| async_tree_memoization_tg  | 240 ms                                                     | 335 ms: 1.40x slower                                       |
| mako                       | 6.99 ms                                                    | 9.85 ms: 1.41x slower                                      |
| float                      | 48.6 ms                                                    | 68.9 ms: 1.42x slower                                      |
| nbody                      | 59.6 ms                                                    | 86.4 ms: 1.45x slower                                      |
| hexiom                     | 4.06 ms                                                    | 6.04 ms: 1.49x slower                                      |
| scimark_sparse_mat_mult    | 2.77 ms                                                    | 4.19 ms: 1.51x slower                                      |
| comprehensions             | 10.2 us                                                    | 15.7 us: 1.54x slower                                      |
| spectral_norm              | 66.4 ms                                                    | 106 ms: 1.59x slower                                       |
| deltablue                  | 2.14 ms                                                    | 3.63 ms: 1.70x slower                                      |
| Geometric mean             | (ref)                                                      | 1.14x slower                                               |

Benchmark hidden because not significant (3): asyncio_websockets, unpickle, asyncio_tcp
Ignored benchmarks (18) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 0.93x