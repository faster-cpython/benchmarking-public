# Results vs. 3.13.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: windows-amd64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.019x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 243 ms: 1.10x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                     |
| html5lib       | 38.9 ms                                                     | 41.5 ms: 1.07x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 97.3 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 259 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 392 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 555 ms: 1.07x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 49.2 ms: 1.39x faster                                                      |
| float          | 49.9 ms                                                     | 44.0 ms: 1.13x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 16.2 ms: 1.32x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.63 ms: 1.04x slower                                                      |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 96.5 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                     |
| xml_etree_generate   | 54.0 ms                                                     | 49.9 ms: 1.08x faster                                                      |
| xml_etree_process    | 37.0 ms                                                     | 35.0 ms: 1.06x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 5.84 ms: 1.01x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 92.9 ms: 1.01x faster                                                      |
| pickle_pure_python   | 190 us                                                      | 198 us: 1.04x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.5 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 4.92 ms: 1.29x faster                                                      |
| django_template | 22.4 ms                                                     | 26.8 ms: 1.20x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                      |
| genshi_xml      | 35.5 ms                                                     | 45.5 ms: 1.28x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 518 us: 16.99x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 15.5 us: 1.50x faster                                                      |
| spectral_norm              | 62.8 ms                                                     | 43.8 ms: 1.43x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 895 us: 1.41x faster                                                       |
| nbody                      | 68.4 ms                                                     | 49.2 ms: 1.39x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 16.2 ms: 1.32x faster                                                      |
| mako                       | 6.35 ms                                                     | 4.92 ms: 1.29x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 61.1 ms: 1.25x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 71.5 ms: 1.21x faster                                                      |
| deepcopy                   | 226 us                                                      | 188 us: 1.21x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 38.7 ms: 1.18x faster                                                      |
| scimark_fft                | 172 ms                                                      | 148 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.80 us: 1.14x faster                                                      |
| float                      | 49.9 ms                                                     | 44.0 ms: 1.13x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.5 ms: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.20 ms: 1.12x faster                                                      |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                     |
| json                       | 3.19 ms                                                     | 2.93 ms: 1.09x faster                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 49.9 ms: 1.08x faster                                                      |
| pyflate                    | 283 ms                                                      | 265 ms: 1.07x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 259 ms: 1.06x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 35.0 ms: 1.06x faster                                                      |
| telco                      | 4.79 ms                                                     | 4.56 ms: 1.05x faster                                                      |
| bench_thread_pool          | 847 us                                                      | 806 us: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.05x faster                                                       |
| fannkuch                   | 253 ms                                                      | 243 ms: 1.04x faster                                                       |
| deltablue                  | 1.92 ms                                                     | 1.84 ms: 1.04x faster                                                      |
| json_dumps                 | 5.92 ms                                                     | 5.84 ms: 1.01x faster                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 92.9 ms: 1.01x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 81.6 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.41 sec: 1.02x slower                                                     |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 75.2 ms: 1.02x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.41 us: 1.02x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 109 us: 1.03x slower                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.63 ms: 1.04x slower                                                      |
| coverage                   | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 392 ms: 1.04x slower                                                       |
| comprehensions             | 10.3 us                                                     | 10.7 us: 1.04x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 198 us: 1.04x slower                                                       |
| tornado_http               | 93.0 ms                                                     | 97.3 ms: 1.05x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 42.8 ms: 1.05x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 55.6 ms: 1.05x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.06x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 43.5 ms: 1.07x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 41.5 ms: 1.07x slower                                                      |
| regex_dna                  | 115 ms                                                      | 123 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 555 ms: 1.07x slower                                                       |
| go                         | 87.0 ms                                                     | 93.2 ms: 1.07x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 58.9 ns: 1.08x slower                                                      |
| pycparser                  | 683 ms                                                      | 736 ms: 1.08x slower                                                       |
| chaos                      | 38.5 ms                                                     | 41.7 ms: 1.08x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 539 ms: 1.09x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 62.2 ms: 1.10x slower                                                      |
| 2to3                       | 221 ms                                                      | 243 ms: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| sympy_str                  | 169 ms                                                      | 192 ms: 1.14x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 99.7 ms: 1.15x slower                                                      |
| sympy_expand               | 291 ms                                                      | 337 ms: 1.16x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 896 us: 1.16x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 203 ms: 1.16x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| generators                 | 19.5 ms                                                     | 22.9 ms: 1.18x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 15.0 ms: 1.20x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 96.5 ms: 1.20x slower                                                      |
| django_template            | 22.4 ms                                                     | 26.8 ms: 1.20x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.16 ms: 1.21x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                     |
| genshi_text                | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 40.8 ms: 1.24x slower                                                      |
| pylint                     | 211 ms                                                      | 268 ms: 1.27x slower                                                       |
| richards_super             | 30.9 ms                                                     | 39.3 ms: 1.27x slower                                                      |
| genshi_xml                 | 35.5 ms                                                     | 45.5 ms: 1.28x slower                                                      |
| raytrace                   | 160 ms                                                      | 207 ms: 1.29x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 5.03 ms: 1.29x slower                                                      |
| richards                   | 27.3 ms                                                     | 37.3 ms: 1.37x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, logging_simple, python_startup_no_site
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.019x faster
# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown