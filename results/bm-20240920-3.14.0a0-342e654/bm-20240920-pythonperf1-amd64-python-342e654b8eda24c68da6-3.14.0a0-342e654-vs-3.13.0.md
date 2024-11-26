# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.025x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 225 ms: 1.02x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 41.4 ms: 1.06x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 84.6 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_none            | 226 ms                                                      | 213 ms: 1.06x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 265 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 566 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 578 ms: 1.11x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.5 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 55.8 ms: 1.12x slower                                                      |
| nbody          | 68.4 ms                                                     | 85.0 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.57 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 92.6 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.3 ms: 1.04x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.16 ms: 1.04x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 58.0 ms: 1.07x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 41.0 ms: 1.11x slower                                                      |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                     |
| pickle_pure_python   | 190 us                                                      | 218 us: 1.15x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| django_template | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                      |
| mako            | 6.35 ms                                                     | 7.11 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 525 us: 16.76x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 884 us: 1.42x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 66.4 ms: 1.30x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.29x faster                                                      |
| deepcopy                   | 226 us                                                      | 193 us: 1.17x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| tornado_http               | 93.0 ms                                                     | 84.6 ms: 1.10x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 21.5 us: 1.08x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 75.6 ms: 1.07x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                                      |
| async_tree_none            | 226 ms                                                      | 213 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| bench_thread_pool          | 847 us                                                      | 811 us: 1.04x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 265 ms: 1.04x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.57 ms: 1.01x faster                                                      |
| go                         | 87.0 ms                                                     | 87.6 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.02x slower                                                       |
| 2to3                       | 221 ms                                                      | 225 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| coverage                   | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.3 ms: 1.04x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.16 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.9 ms                                                     | 90.7 ms: 1.04x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.45 sec: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 43.2 ms: 1.06x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 41.4 ms: 1.06x slower                                                      |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                      |
| sympy_expand               | 291 ms                                                      | 310 ms: 1.06x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 78.4 ms: 1.07x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 58.0 ms: 1.07x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.42 us: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| crypto_pyaes               | 45.4 ms                                                     | 49.2 ms: 1.08x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 566 ms: 1.09x slower                                                       |
| pycparser                  | 683 ms                                                      | 747 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 192 ms: 1.10x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.91 us: 1.10x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 36.4 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 578 ms: 1.11x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 41.0 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 548 ms: 1.11x slower                                                       |
| django_template            | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                      |
| float                      | 49.9 ms                                                     | 55.8 ms: 1.12x slower                                                      |
| mako                       | 6.35 ms                                                     | 7.11 ms: 1.12x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                     |
| spectral_norm              | 62.8 ms                                                     | 70.5 ms: 1.12x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.39 ms: 1.13x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                     |
| nqueens                    | 56.7 ms                                                     | 64.4 ms: 1.14x slower                                                      |
| pyflate                    | 283 ms                                                      | 322 ms: 1.14x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.5 ms: 1.14x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.46 ms: 1.15x slower                                                      |
| chaos                      | 38.5 ms                                                     | 44.2 ms: 1.15x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 218 us: 1.15x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 92.6 ms: 1.15x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 63.4 ns: 1.16x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 896 us: 1.16x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 61.7 ms: 1.17x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.12 ms: 1.17x slower                                                      |
| richards_super             | 30.9 ms                                                     | 36.1 ms: 1.17x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.1 ms: 1.18x slower                                                      |
| fannkuch                   | 253 ms                                                      | 300 ms: 1.18x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.93 ms: 1.19x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.30 ms: 1.20x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 92.5 ms: 1.21x slower                                                      |
| scimark_fft                | 172 ms                                                      | 212 ms: 1.23x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 50.6 ms: 1.24x slower                                                      |
| nbody                      | 68.4 ms                                                     | 85.0 ms: 1.24x slower                                                      |
| raytrace                   | 160 ms                                                      | 201 ms: 1.25x slower                                                       |
| json                       | 3.19 ms                                                     | 4.04 ms: 1.27x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, python_startup_no_site, xml_etree_parse, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown