# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 225 ms: 1.04x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.6 ms                                                     | 41.4 ms: 1.07x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 84.6 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 467 ms: 1.40x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_none            | 223 ms                                                      | 213 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 566 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 578 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 48.1 ms                                                     | 55.8 ms: 1.16x slower                                                      |
| nbody          | 64.5 ms                                                     | 85.0 ms: 1.32x slower                                                      |
| Geometric mean | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| regex_dna      | 114 ms                                                      | 117 ms: 1.03x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 92.6 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.19 us: 1.02x faster                                                      |
| unpickle_list        | 2.72 us                                                     | 2.75 us: 1.01x slower                                                      |
| pickle_dict          | 18.0 us                                                     | 18.5 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.3 ms: 1.03x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.16 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 58.0 ms: 1.09x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.51 us: 1.10x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.0 ms: 1.12x slower                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| pickle_pure_python   | 183 us                                                      | 218 us: 1.19x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 155 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 35.4 ms: 1.08x slower                                                      |
| mako            | 6.24 ms                                                     | 7.11 ms: 1.14x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.0 ms: 1.14x slower                                                      |
| django_template | 21.8 ms                                                     | 24.9 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 525 us: 16.53x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 467 ms: 1.40x faster                                                       |
| deepcopy                   | 223 us                                                      | 193 us: 1.16x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 84.6 ms: 1.10x faster                                                      |
| pathlib                    | 81.2 ms                                                     | 75.6 ms: 1.07x faster                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 66.4 ms: 1.05x faster                                                      |
| async_tree_none            | 223 ms                                                      | 213 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| bench_thread_pool          | 828 us                                                      | 811 us: 1.02x faster                                                       |
| pickle                     | 7.34 us                                                     | 7.19 us: 1.02x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.53 ms: 1.02x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 21.5 us: 1.01x faster                                                      |
| regex_v8                   | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.75 us: 1.01x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.3 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| sqlite_synth               | 1.60 us                                                     | 1.62 us: 1.01x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                      |
| regex_dna                  | 114 ms                                                      | 117 ms: 1.03x slower                                                       |
| pickle_dict                | 18.0 us                                                     | 18.5 us: 1.03x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.3 ms: 1.03x slower                                                      |
| go                         | 84.6 ms                                                     | 87.6 ms: 1.04x slower                                                      |
| 2to3                       | 217 ms                                                      | 225 ms: 1.04x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 90.7 ms: 1.05x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.45 sec: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.05x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 884 us: 1.07x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.16 ms: 1.07x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 43.2 ms: 1.07x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 41.4 ms: 1.07x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 43.1 ns: 1.08x slower                                                      |
| sympy_str                  | 166 ms                                                      | 179 ms: 1.08x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| genshi_xml                 | 32.8 ms                                                     | 35.4 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 78.4 ms: 1.08x slower                                                      |
| sympy_expand               | 285 ms                                                      | 310 ms: 1.09x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 58.0 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 36.4 ms: 1.10x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.51 us: 1.10x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 566 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 111 us: 1.11x slower                                                       |
| async_tree_io              | 521 ms                                                      | 578 ms: 1.11x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.39 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 548 ms: 1.11x slower                                                       |
| logging_simple             | 5.72 us                                                     | 6.42 us: 1.12x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 192 ms: 1.12x slower                                                       |
| logging_format             | 6.15 us                                                     | 6.91 us: 1.12x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.0 ms: 1.12x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| mako                       | 6.24 ms                                                     | 7.11 ms: 1.14x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 17.0 ms: 1.14x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 61.7 ms: 1.14x slower                                                      |
| django_template            | 21.8 ms                                                     | 24.9 ms: 1.14x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 49.2 ms: 1.15x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 92.6 ms: 1.16x slower                                                      |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.16x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| float                      | 48.1 ms                                                     | 55.8 ms: 1.16x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 64.4 ms: 1.16x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| chaos                      | 37.9 ms                                                     | 44.2 ms: 1.17x slower                                                      |
| pyflate                    | 275 ms                                                      | 322 ms: 1.17x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.12 ms: 1.17x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 896 us: 1.18x slower                                                       |
| pickle_pure_python         | 183 us                                                      | 218 us: 1.19x slower                                                       |
| spectral_norm              | 59.2 ms                                                     | 70.5 ms: 1.19x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.46 ms: 1.21x slower                                                      |
| scimark_fft                | 174 ms                                                      | 212 ms: 1.22x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 155 us: 1.22x slower                                                       |
| fannkuch                   | 245 ms                                                      | 300 ms: 1.22x slower                                                       |
| richards_super             | 29.3 ms                                                     | 36.1 ms: 1.23x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.30 ms: 1.23x slower                                                      |
| richards                   | 26.0 ms                                                     | 32.1 ms: 1.23x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 63.4 ns: 1.24x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.93 ms: 1.25x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 50.6 ms: 1.26x slower                                                      |
| raytrace                   | 156 ms                                                      | 201 ms: 1.28x slower                                                       |
| scimark_sor                | 72.0 ms                                                     | 92.5 ms: 1.28x slower                                                      |
| nbody                      | 64.5 ms                                                     | 85.0 ms: 1.32x slower                                                      |
| json                       | 2.98 ms                                                     | 4.04 ms: 1.36x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (10): async_tree_memoization, pycparser, async_tree_none_tg, python_startup, xml_etree_parse, async_tree_cpu_io_mixed, json_loads, asyncio_tcp_ssl, pickle_list, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown