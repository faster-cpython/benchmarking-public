# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.021x faster
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 243 ms: 1.10x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.94 sec: 1.24x slower                                                     |
| html5lib       | 38.9 ms                                                     | 42.8 ms: 1.10x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 99.1 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                       |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 251 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 198 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 384 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 395 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 559 ms: 1.08x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                      |
| async_tree_io              | 521 ms                                                      | 586 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 50.0 ms: 1.37x faster                                                      |
| float          | 49.9 ms                                                     | 45.3 ms: 1.10x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.0 ms: 1.43x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                                      |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 95.6 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.27 sec: 1.10x faster                                                     |
| xml_etree_generate   | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_process    | 37.0 ms                                                     | 35.8 ms: 1.03x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 5.78 ms: 1.02x faster                                                      |
| pickle_pure_python   | 190 us                                                      | 195 us: 1.03x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 18.6 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.26 ms: 1.21x faster                                                      |
| django_template | 22.4 ms                                                     | 26.8 ms: 1.20x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 19.7 ms: 1.26x slower                                                      |
| genshi_xml      | 35.5 ms                                                     | 46.3 ms: 1.30x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 519 us: 16.94x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 15.0 us: 1.55x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 15.0 ms: 1.43x faster                                                      |
| spectral_norm              | 62.8 ms                                                     | 44.1 ms: 1.42x faster                                                      |
| nbody                      | 68.4 ms                                                     | 50.0 ms: 1.37x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 933 us: 1.35x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 60.5 ms: 1.26x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.58 ms: 1.25x faster                                                      |
| deepcopy                   | 226 us                                                      | 183 us: 1.24x faster                                                       |
| mako                       | 6.35 ms                                                     | 5.26 ms: 1.21x faster                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 38.2 ms: 1.19x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 74.4 ms: 1.16x faster                                                      |
| scimark_fft                | 172 ms                                                      | 149 ms: 1.15x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.81 us: 1.14x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.18 ms: 1.12x faster                                                      |
| float                      | 49.9 ms                                                     | 45.3 ms: 1.10x faster                                                      |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 251 ms: 1.10x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.27 sec: 1.10x faster                                                     |
| json                       | 3.19 ms                                                     | 2.93 ms: 1.09x faster                                                      |
| pyflate                    | 283 ms                                                      | 262 ms: 1.08x faster                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                      |
| fannkuch                   | 253 ms                                                      | 239 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| deltablue                  | 1.92 ms                                                     | 1.82 ms: 1.05x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 198 ms: 1.05x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.58 ms: 1.05x faster                                                      |
| xml_etree_process          | 37.0 ms                                                     | 35.8 ms: 1.03x faster                                                      |
| json_dumps                 | 5.92 ms                                                     | 5.78 ms: 1.02x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 79.1 ms: 1.02x faster                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 74.6 ms: 1.01x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.05 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 384 ms: 1.02x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 54.0 ms: 1.02x slower                                                      |
| python_startup_no_site     | 18.1 ms                                                     | 18.6 ms: 1.03x slower                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 195 us: 1.03x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 507 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 395 ms: 1.03x slower                                                       |
| coverage                   | 45.6 ms                                                     | 47.6 ms: 1.04x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.05 sec: 1.05x slower                                                     |
| logging_format             | 6.26 us                                                     | 6.56 us: 1.05x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 57.3 ns: 1.05x slower                                                      |
| comprehensions             | 10.3 us                                                     | 10.8 us: 1.05x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.46 sec: 1.05x slower                                                     |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                       |
| chaos                      | 38.5 ms                                                     | 40.7 ms: 1.06x slower                                                      |
| go                         | 87.0 ms                                                     | 92.0 ms: 1.06x slower                                                      |
| tornado_http               | 93.0 ms                                                     | 99.1 ms: 1.07x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 43.5 ms: 1.07x slower                                                      |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 559 ms: 1.08x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 44.0 ms: 1.08x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 61.4 ms: 1.08x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                       |
| 2to3                       | 221 ms                                                      | 243 ms: 1.10x slower                                                       |
| pycparser                  | 683 ms                                                      | 750 ms: 1.10x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 42.8 ms: 1.10x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                                      |
| async_tree_io              | 521 ms                                                      | 586 ms: 1.12x slower                                                       |
| sympy_str                  | 169 ms                                                      | 190 ms: 1.12x slower                                                       |
| sympy_expand               | 291 ms                                                      | 329 ms: 1.13x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 99.3 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 203 ms: 1.16x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 901 us: 1.17x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 95.6 ms: 1.19x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 15.0 ms: 1.20x slower                                                      |
| django_template            | 22.4 ms                                                     | 26.8 ms: 1.20x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 40.0 ms: 1.22x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.17 ms: 1.22x slower                                                      |
| raytrace                   | 160 ms                                                      | 198 ms: 1.23x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.94 sec: 1.24x slower                                                     |
| hexiom                     | 3.89 ms                                                     | 4.87 ms: 1.25x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 19.7 ms: 1.26x slower                                                      |
| richards_super             | 30.9 ms                                                     | 39.3 ms: 1.27x slower                                                      |
| pylint                     | 211 ms                                                      | 269 ms: 1.28x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 46.3 ms: 1.30x slower                                                      |
| richards                   | 27.3 ms                                                     | 36.0 ms: 1.32x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, xml_etree_iterparse, xml_etree_parse
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 99.39% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown