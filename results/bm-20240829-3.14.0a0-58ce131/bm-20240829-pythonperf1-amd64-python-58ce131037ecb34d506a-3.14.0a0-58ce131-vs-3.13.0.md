# Results vs. 3.13.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-amd64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 230 ms: 1.06x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 40.1 ms: 1.04x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 538 ms: 1.21x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 213 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 402 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 571 ms: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 57.0 ms: 1.19x slower                                                      |
| nbody          | 64.5 ms                                                     | 89.2 ms: 1.38x slower                                                      |
| Geometric mean | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.64 ms: 1.01x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 15.6 ms: 1.06x slower                                                      |
| regex_dna      | 114 ms                                                      | 124 ms: 1.09x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 91.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.8 ms: 1.06x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.28 ms: 1.09x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.5 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.9 ms: 1.15x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 217 us: 1.18x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.65 sec: 1.21x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 155 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.0 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.4 ms: 1.11x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.9 ms: 1.14x slower                                                      |
| mako            | 6.24 ms                                                     | 7.17 ms: 1.15x slower                                                      |
| django_template | 21.8 ms                                                     | 25.0 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 522 us: 16.61x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 538 ms: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 192 us: 1.16x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 213 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 21.3 us: 1.02x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 93.8 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.64 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.0 ms: 1.01x slower                                                      |
| json                       | 2.98 ms                                                     | 3.02 ms: 1.01x slower                                                      |
| go                         | 84.6 ms                                                     | 87.6 ms: 1.04x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 40.1 ms: 1.04x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 91.1 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.8 ms: 1.06x slower                                                      |
| coverage                   | 46.7 ms                                                     | 49.4 ms: 1.06x slower                                                      |
| 2to3                       | 217 ms                                                      | 230 ms: 1.06x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.14 ms: 1.06x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.6 ms: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 402 ms: 1.07x slower                                                       |
| sympy_str                  | 166 ms                                                      | 178 ms: 1.07x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 43.5 ms: 1.08x slower                                                      |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| mdp                        | 1.38 sec                                                    | 1.50 sec: 1.08x slower                                                     |
| meteor_contest             | 72.3 ms                                                     | 78.3 ms: 1.08x slower                                                      |
| regex_dna                  | 114 ms                                                      | 124 ms: 1.09x slower                                                       |
| pycparser                  | 758 ms                                                      | 824 ms: 1.09x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.28 ms: 1.09x slower                                                      |
| sympy_expand               | 285 ms                                                      | 311 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 110 us: 1.10x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.77 us: 1.10x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 913 us: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.34 us: 1.11x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 36.4 ms: 1.11x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 571 ms: 1.11x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 59.5 ms: 1.12x slower                                                      |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 37.0 ms: 1.12x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 16.9 ms: 1.14x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 91.2 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 195 ms: 1.14x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 562 ms: 1.14x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 41.9 ms: 1.15x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.17 ms: 1.15x slower                                                      |
| django_template            | 21.8 ms                                                     | 25.0 ms: 1.15x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 49.6 ms: 1.16x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.15 sec: 1.16x slower                                                     |
| chaos                      | 37.9 ms                                                     | 44.2 ms: 1.17x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 69.9 ms: 1.18x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 217 us: 1.18x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 65.8 ms: 1.18x slower                                                      |
| float                      | 48.1 ms                                                     | 57.0 ms: 1.19x slower                                                      |
| comprehensions             | 10.2 us                                                     | 12.2 us: 1.19x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.14 ms: 1.19x slower                                                      |
| pyflate                    | 275 ms                                                      | 329 ms: 1.19x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 64.6 ms: 1.20x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 913 us: 1.20x slower                                                       |
| raytrace                   | 156 ms                                                      | 189 ms: 1.21x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.65 sec: 1.21x slower                                                     |
| unpickle_pure_python       | 127 us                                                      | 155 us: 1.22x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.53 ms: 1.23x slower                                                      |
| scimark_fft                | 174 ms                                                      | 214 ms: 1.23x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.30 ms: 1.23x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.89 ms: 1.24x slower                                                      |
| fannkuch                   | 245 ms                                                      | 303 ms: 1.24x slower                                                       |
| richards                   | 26.0 ms                                                     | 32.6 ms: 1.25x slower                                                      |
| richards_super             | 29.3 ms                                                     | 36.9 ms: 1.26x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 64.4 ns: 1.26x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 52.4 ms: 1.30x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 95.7 ms: 1.33x slower                                                      |
| nbody                      | 64.5 ms                                                     | 89.2 ms: 1.38x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, async_tree_memoization, bench_thread_pool, bench_mp_pool, async_tree_none_tg, python_startup, json_loads, async_tree_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown