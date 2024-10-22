# Results vs. 3.13.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: windows-amd64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.01x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 243 ms: 1.12x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.22x slower                                                     |
| html5lib       | 38.6 ms                                                     | 41.5 ms: 1.08x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 97.3 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 542 ms: 1.21x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.08x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.53 sec: 1.07x faster                                                     |
| async_tree_memoization     | 271 ms                                                      | 259 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 392 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 555 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.2 ms: 1.31x faster                                                      |
| float          | 48.1 ms                                                     | 44.0 ms: 1.09x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| regex_dna      | 114 ms                                                      | 123 ms: 1.08x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 16.2 ms: 1.11x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 96.5 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 53.3 ms                                                     | 49.9 ms: 1.07x faster                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.28 sec: 1.07x faster                                                     |
| xml_etree_process    | 36.5 ms                                                     | 35.0 ms: 1.04x faster                                                      |
| pickle_dict          | 18.0 us                                                     | 17.7 us: 1.02x faster                                                      |
| pickle               | 7.34 us                                                     | 7.31 us: 1.00x faster                                                      |
| json_dumps           | 5.76 ms                                                     | 5.84 ms: 1.01x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.82 us: 1.04x slower                                                      |
| unpickle             | 8.63 us                                                     | 9.16 us: 1.06x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 198 us: 1.08x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 141 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle_list, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.5 ms: 1.02x slower                                                      |
| python_startup_no_site | 17.8 ms                                                     | 18.3 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 4.92 ms: 1.27x faster                                                      |
| django_template | 21.8 ms                                                     | 26.8 ms: 1.23x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 19.2 ms: 1.29x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 45.5 ms: 1.39x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 518 us: 16.76x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 15.5 us: 1.41x faster                                                      |
| spectral_norm              | 59.2 ms                                                     | 43.8 ms: 1.35x faster                                                      |
| nbody                      | 64.5 ms                                                     | 49.2 ms: 1.31x faster                                                      |
| mako                       | 6.24 ms                                                     | 4.92 ms: 1.27x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 542 ms: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                       |
| scimark_sor                | 72.0 ms                                                     | 61.1 ms: 1.18x faster                                                      |
| scimark_fft                | 174 ms                                                      | 148 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 38.7 ms: 1.11x faster                                                      |
| float                      | 48.1 ms                                                     | 44.0 ms: 1.09x faster                                                      |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.08x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.53 sec: 1.07x faster                                                     |
| xml_etree_generate         | 53.3 ms                                                     | 49.9 ms: 1.07x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.28 sec: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.20 ms: 1.06x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.56 ms: 1.06x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 259 ms: 1.05x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 35.0 ms: 1.04x faster                                                      |
| pyflate                    | 275 ms                                                      | 265 ms: 1.04x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 806 us: 1.03x faster                                                       |
| json                       | 2.98 ms                                                     | 2.93 ms: 1.02x faster                                                      |
| pickle_dict                | 18.0 us                                                     | 17.7 us: 1.02x faster                                                      |
| deltablue                  | 1.86 ms                                                     | 1.84 ms: 1.01x faster                                                      |
| fannkuch                   | 245 ms                                                      | 243 ms: 1.01x faster                                                       |
| pickle                     | 7.34 us                                                     | 7.31 us: 1.00x faster                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.3 ms: 1.01x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 5.84 ms: 1.01x slower                                                      |
| python_startup             | 22.2 ms                                                     | 22.5 ms: 1.02x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.41 sec: 1.02x slower                                                     |
| bench_mp_pool              | 69.6 ms                                                     | 71.5 ms: 1.03x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.3 ms: 1.03x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 55.6 ms: 1.03x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.82 us: 1.04x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 75.2 ms: 1.04x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.41 us: 1.04x slower                                                      |
| logging_simple             | 5.72 us                                                     | 5.97 us: 1.04x slower                                                      |
| comprehensions             | 10.2 us                                                     | 10.7 us: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 392 ms: 1.05x slower                                                       |
| tornado_http               | 92.8 ms                                                     | 97.3 ms: 1.05x slower                                                      |
| unpickle                   | 8.63 us                                                     | 9.16 us: 1.06x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 42.8 ms: 1.06x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 41.5 ms: 1.08x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 43.5 ms: 1.08x slower                                                      |
| regex_dna                  | 114 ms                                                      | 123 ms: 1.08x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 895 us: 1.08x slower                                                       |
| pickle_pure_python         | 183 us                                                      | 198 us: 1.08x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 109 us: 1.08x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 555 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 539 ms: 1.09x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.7 ms: 1.10x slower                                                      |
| go                         | 84.6 ms                                                     | 93.2 ms: 1.10x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 16.2 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 141 us: 1.11x slower                                                       |
| 2to3                       | 217 ms                                                      | 243 ms: 1.12x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 62.2 ms: 1.12x slower                                                      |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.12x slower                                                      |
| pprint_pformat             | 991 ms                                                      | 1.12 sec: 1.13x slower                                                     |
| sympy_sum                  | 86.4 ms                                                     | 99.7 ms: 1.15x slower                                                      |
| sympy_str                  | 166 ms                                                      | 192 ms: 1.15x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 58.9 ns: 1.15x slower                                                      |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 896 us: 1.18x slower                                                       |
| generators                 | 19.5 ms                                                     | 22.9 ms: 1.18x slower                                                      |
| sympy_expand               | 285 ms                                                      | 337 ms: 1.18x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 203 ms: 1.19x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 96.5 ms: 1.20x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 15.0 ms: 1.22x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.16 ms: 1.22x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.22x slower                                                     |
| django_template            | 21.8 ms                                                     | 26.8 ms: 1.23x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 40.8 ms: 1.23x slower                                                      |
| pylint                     | 211 ms                                                      | 268 ms: 1.27x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 19.2 ms: 1.29x slower                                                      |
| raytrace                   | 156 ms                                                      | 207 ms: 1.32x slower                                                       |
| richards_super             | 29.3 ms                                                     | 39.3 ms: 1.34x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 5.03 ms: 1.36x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 45.5 ms: 1.39x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 56.3 ns: 1.41x slower                                                      |
| richards                   | 26.0 ms                                                     | 37.3 ms: 1.43x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (10): async_tree_none_tg, pycparser, xml_etree_iterparse, pickle_list, xml_etree_parse, sqlite_synth, gc_traversal, json_loads, pathlib, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown