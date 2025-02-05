# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.031x faster
- HPT reliability: 97.23%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 239 ms: 1.08x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                     |
| html5lib       | 38.9 ms                                                     | 42.1 ms: 1.08x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 87.4 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                       |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 258 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 197 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 394 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 555 ms: 1.07x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                      |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 49.4 ms: 1.38x faster                                                      |
| float          | 49.9 ms                                                     | 44.5 ms: 1.12x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.9 ms: 1.43x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 94.2 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.26 sec: 1.11x faster                                                     |
| xml_etree_generate   | 54.0 ms                                                     | 49.0 ms: 1.10x faster                                                      |
| xml_etree_process    | 37.0 ms                                                     | 34.8 ms: 1.06x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 5.73 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 60.7 ms: 1.02x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 92.4 ms: 1.01x faster                                                      |
| pickle_pure_python   | 190 us                                                      | 196 us: 1.03x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 21.6 ms: 1.18x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.26 ms: 1.21x faster                                                      |
| django_template | 22.4 ms                                                     | 26.2 ms: 1.17x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 18.9 ms: 1.21x slower                                                      |
| genshi_xml      | 35.5 ms                                                     | 45.7 ms: 1.29x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 525 us: 16.74x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 14.8 us: 1.57x faster                                                      |
| spectral_norm              | 62.8 ms                                                     | 43.3 ms: 1.45x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.9 ms: 1.43x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 901 us: 1.40x faster                                                       |
| nbody                      | 68.4 ms                                                     | 49.4 ms: 1.38x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 60.7 ms: 1.26x faster                                                      |
| deepcopy                   | 226 us                                                      | 181 us: 1.25x faster                                                       |
| mako                       | 6.35 ms                                                     | 5.26 ms: 1.21x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 71.7 ms: 1.21x faster                                                      |
| python_startup             | 25.4 ms                                                     | 21.6 ms: 1.18x faster                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 38.6 ms: 1.18x faster                                                      |
| scimark_fft                | 172 ms                                                      | 149 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.13 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.79 us: 1.15x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                       |
| float                      | 49.9 ms                                                     | 44.5 ms: 1.12x faster                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.26 sec: 1.11x faster                                                     |
| xml_etree_generate         | 54.0 ms                                                     | 49.0 ms: 1.10x faster                                                      |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                       |
| json                       | 3.19 ms                                                     | 2.95 ms: 1.08x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 74.8 ms: 1.08x faster                                                      |
| pyflate                    | 283 ms                                                      | 265 ms: 1.07x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 258 ms: 1.07x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 34.8 ms: 1.06x faster                                                      |
| tornado_http               | 93.0 ms                                                     | 87.4 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 197 ms: 1.06x faster                                                       |
| deltablue                  | 1.92 ms                                                     | 1.82 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| bench_thread_pool          | 847 us                                                      | 809 us: 1.05x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.60 ms: 1.04x faster                                                      |
| json_dumps                 | 5.92 ms                                                     | 5.73 ms: 1.03x faster                                                      |
| fannkuch                   | 253 ms                                                      | 248 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 60.7 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 92.4 ms: 1.01x faster                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.06 us: 1.02x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 74.9 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 503 ms: 1.02x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 54.4 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 394 ms: 1.03x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.45 us: 1.03x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.43 sec: 1.03x slower                                                     |
| pprint_pformat             | 999 ms                                                      | 1.03 sec: 1.03x slower                                                     |
| pickle_pure_python         | 190 us                                                      | 196 us: 1.03x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 42.3 ms: 1.04x slower                                                      |
| chaos                      | 38.5 ms                                                     | 40.0 ms: 1.04x slower                                                      |
| comprehensions             | 10.3 us                                                     | 10.7 us: 1.04x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 42.7 ms: 1.05x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 57.2 ns: 1.05x slower                                                      |
| pycparser                  | 683 ms                                                      | 715 ms: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 59.6 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| coverage                   | 45.6 ms                                                     | 48.1 ms: 1.06x slower                                                      |
| go                         | 87.0 ms                                                     | 92.2 ms: 1.06x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 555 ms: 1.07x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 42.1 ms: 1.08x slower                                                      |
| 2to3                       | 221 ms                                                      | 239 ms: 1.08x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                       |
| sympy_str                  | 169 ms                                                      | 189 ms: 1.12x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 97.9 ms: 1.13x slower                                                      |
| sympy_expand               | 291 ms                                                      | 330 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 199 ms: 1.14x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 886 us: 1.15x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.16x slower                                                       |
| django_template            | 22.4 ms                                                     | 26.2 ms: 1.17x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 94.2 ms: 1.17x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 14.8 ms: 1.19x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.20x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 39.7 ms: 1.21x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 18.9 ms: 1.21x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                     |
| pylint                     | 211 ms                                                      | 263 ms: 1.25x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.89 ms: 1.26x slower                                                      |
| raytrace                   | 160 ms                                                      | 202 ms: 1.26x slower                                                       |
| richards_super             | 30.9 ms                                                     | 39.1 ms: 1.27x slower                                                      |
| genshi_xml                 | 35.5 ms                                                     | 45.7 ms: 1.29x slower                                                      |
| richards                   | 27.3 ms                                                     | 36.5 ms: 1.34x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 97.23% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown