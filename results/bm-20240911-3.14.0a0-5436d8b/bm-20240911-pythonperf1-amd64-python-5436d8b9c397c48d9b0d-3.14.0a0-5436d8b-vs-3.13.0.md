# Results vs. 3.13.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-amd64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 221 ms: 1.02x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 39.4 ms: 1.02x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 83.3 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 464 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.49 sec: 1.10x faster                                                     |
| async_tree_none            | 223 ms                                                      | 207 ms: 1.08x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 259 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 390 ms: 1.04x slower                                                       |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 553 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 54.4 ms: 1.13x slower                                                      |
| nbody          | 64.5 ms                                                     | 79.8 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 14.6 ms: 1.01x faster                                                      |
| regex_compile  | 80.1 ms                                                     | 89.6 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.28 us: 1.01x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.77 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.8 ms: 1.04x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.18 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 57.2 ms: 1.07x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.43 us: 1.09x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 19.7 us: 1.09x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.4 ms: 1.11x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 145 us: 1.14x slower                                                       |
| pickle_pure_python   | 183 us                                                      | 209 us: 1.14x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 21.3 ms: 1.04x faster                                                      |
| python_startup_no_site | 17.8 ms                                                     | 17.3 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.9 ms: 1.09x slower                                                      |
| mako            | 6.24 ms                                                     | 6.83 ms: 1.10x slower                                                      |
| django_template | 21.8 ms                                                     | 24.5 ms: 1.13x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 16.9 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 507 us: 17.11x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 464 ms: 1.41x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 83.3 ms: 1.11x faster                                                      |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.49 sec: 1.10x faster                                                     |
| pathlib                    | 81.2 ms                                                     | 73.9 ms: 1.10x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 20.0 us: 1.09x faster                                                      |
| async_tree_none            | 223 ms                                                      | 207 ms: 1.08x faster                                                       |
| bench_mp_pool              | 69.6 ms                                                     | 65.8 ms: 1.06x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 259 ms: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 197 ms: 1.04x faster                                                       |
| python_startup             | 22.2 ms                                                     | 21.3 ms: 1.04x faster                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 17.3 ms: 1.03x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.52 ms: 1.02x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 810 us: 1.02x faster                                                       |
| pickle                     | 7.34 us                                                     | 7.28 us: 1.01x faster                                                      |
| regex_v8                   | 14.7 ms                                                     | 14.6 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.62 us: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| unpickle_list              | 2.72 us                                                     | 2.77 us: 1.02x slower                                                      |
| 2to3                       | 217 ms                                                      | 221 ms: 1.02x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 39.4 ms: 1.02x slower                                                      |
| coverage                   | 46.7 ms                                                     | 48.1 ms: 1.03x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 89.2 ms: 1.03x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 41.3 ns: 1.03x slower                                                      |
| json                       | 2.98 ms                                                     | 3.09 ms: 1.04x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 41.9 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.8 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 390 ms: 1.04x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.06 ms: 1.04x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.0 ms: 1.06x slower                                                      |
| sympy_str                  | 166 ms                                                      | 176 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 887 us: 1.07x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.18 ms: 1.07x slower                                                      |
| sympy_expand               | 285 ms                                                      | 306 ms: 1.07x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 57.2 ms: 1.07x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 77.6 ms: 1.07x slower                                                      |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| async_tree_io_tg           | 512 ms                                                      | 553 ms: 1.08x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.66 us: 1.08x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.50 sec: 1.08x slower                                                     |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.0 ms: 1.09x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.25 us: 1.09x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.43 us: 1.09x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 64.7 ms: 1.09x slower                                                      |
| pickle_dict                | 18.0 us                                                     | 19.7 us: 1.09x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 35.9 ms: 1.09x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 46.9 ms: 1.09x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.83 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 541 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.10x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.4 ms: 1.11x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.4 us: 1.11x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 191 ms: 1.12x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.3 ms: 1.12x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 89.6 ms: 1.12x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.11 sec: 1.12x slower                                                     |
| django_template            | 21.8 ms                                                     | 24.5 ms: 1.13x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.64 ms: 1.13x slower                                                      |
| float                      | 48.1 ms                                                     | 54.4 ms: 1.13x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 62.9 ms: 1.13x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 16.9 ms: 1.14x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 145 us: 1.14x slower                                                       |
| pickle_pure_python         | 183 us                                                      | 209 us: 1.14x slower                                                       |
| fannkuch                   | 245 ms                                                      | 280 ms: 1.14x slower                                                       |
| scimark_lu                 | 54.0 ms                                                     | 61.8 ms: 1.14x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| pyflate                    | 275 ms                                                      | 315 ms: 1.14x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.09 ms: 1.15x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 875 us: 1.15x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.30 ms: 1.16x slower                                                      |
| scimark_fft                | 174 ms                                                      | 204 ms: 1.17x slower                                                       |
| raytrace                   | 156 ms                                                      | 187 ms: 1.20x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.24 ms: 1.20x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 48.5 ms: 1.20x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 61.9 ns: 1.21x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 87.5 ms: 1.22x slower                                                      |
| richards                   | 26.0 ms                                                     | 31.7 ms: 1.22x slower                                                      |
| richards_super             | 29.3 ms                                                     | 35.8 ms: 1.22x slower                                                      |
| nbody                      | 64.5 ms                                                     | 79.8 ms: 1.24x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (7): pycparser, regex_dna, go, async_tree_cpu_io_mixed, xml_etree_parse, pickle_list, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown