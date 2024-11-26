# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-amd64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.022x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 223 ms: 1.01x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                     |
| html5lib       | 38.9 ms                                                     | 42.2 ms: 1.08x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                                       |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 261 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 201 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 565 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 574 ms: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 55.9 ms: 1.12x slower                                                      |
| nbody          | 68.4 ms                                                     | 82.0 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.57 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 91.4 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 6.19 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.7 ms: 1.05x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.6 ms: 1.07x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 41.0 ms: 1.11x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 213 us: 1.12x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 21.9 ms: 1.16x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 17.7 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 16.8 ms: 1.08x slower                                                      |
| mako            | 6.35 ms                                                     | 7.03 ms: 1.11x slower                                                      |
| django_template | 22.4 ms                                                     | 25.1 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 525 us: 16.75x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 890 us: 1.41x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.54 ms: 1.28x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 68.8 ms: 1.26x faster                                                      |
| deepcopy                   | 226 us                                                      | 187 us: 1.21x faster                                                       |
| python_startup             | 25.4 ms                                                     | 21.9 ms: 1.16x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 20.9 us: 1.11x faster                                                      |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.91 us: 1.08x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 261 ms: 1.06x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 802 us: 1.06x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 201 ms: 1.04x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| python_startup_no_site     | 18.1 ms                                                     | 17.7 ms: 1.02x faster                                                      |
| go                         | 87.0 ms                                                     | 85.9 ms: 1.01x faster                                                      |
| tornado_http               | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.57 ms: 1.01x faster                                                      |
| 2to3                       | 221 ms                                                      | 223 ms: 1.01x slower                                                       |
| coverage                   | 45.6 ms                                                     | 46.0 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.01x slower                                                       |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| telco                      | 4.79 ms                                                     | 4.89 ms: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 90.1 ms: 1.04x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.44 sec: 1.04x slower                                                     |
| typing_runtime_protocols   | 105 us                                                      | 110 us: 1.04x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.19 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.7 ms: 1.05x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 77.4 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.29 us: 1.06x slower                                                      |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                       |
| pycparser                  | 683 ms                                                      | 723 ms: 1.06x slower                                                       |
| sympy_expand               | 291 ms                                                      | 310 ms: 1.07x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 43.5 ms: 1.07x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 57.6 ms: 1.07x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                     |
| logging_format             | 6.26 us                                                     | 6.73 us: 1.08x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 16.8 ms: 1.08x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 42.2 ms: 1.08x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 565 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 192 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 574 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 50.2 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 546 ms: 1.11x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| mako                       | 6.35 ms                                                     | 7.03 ms: 1.11x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 41.0 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                       |
| float                      | 49.9 ms                                                     | 55.9 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.75 ms: 1.12x slower                                                      |
| django_template            | 22.4 ms                                                     | 25.1 ms: 1.12x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 213 us: 1.12x slower                                                       |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| chaos                      | 38.5 ms                                                     | 43.6 ms: 1.13x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 91.4 ms: 1.13x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.43 ms: 1.14x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 71.5 ms: 1.14x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 62.3 ns: 1.14x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 64.7 ms: 1.14x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 885 us: 1.15x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.10 ms: 1.15x slower                                                      |
| pyflate                    | 283 ms                                                      | 328 ms: 1.16x slower                                                       |
| richards                   | 27.3 ms                                                     | 32.0 ms: 1.17x slower                                                      |
| comprehensions             | 10.3 us                                                     | 12.0 us: 1.17x slower                                                      |
| richards_super             | 30.9 ms                                                     | 36.2 ms: 1.17x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.28 ms: 1.19x slower                                                      |
| nbody                      | 68.4 ms                                                     | 82.0 ms: 1.20x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 91.3 ms: 1.20x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 63.7 ms: 1.20x slower                                                      |
| fannkuch                   | 253 ms                                                      | 305 ms: 1.21x slower                                                       |
| scimark_fft                | 172 ms                                                      | 209 ms: 1.21x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.5 ms: 1.21x slower                                                      |
| raytrace                   | 160 ms                                                      | 201 ms: 1.26x slower                                                       |
| json                       | 3.19 ms                                                     | 4.33 ms: 1.36x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.022x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown