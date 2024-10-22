# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.00x slower
- HPT reliability: 99.31%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 241 ms: 1.11x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                                     |
| html5lib       | 38.6 ms                                                     | 41.9 ms: 1.08x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 87.6 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 480 ms: 1.36x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.37 sec: 1.19x faster                                                     |
| async_tree_memoization_tg  | 288 ms                                                      | 256 ms: 1.12x faster                                                       |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.09x faster                                                       |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 198 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 395 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 562 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.16x slower                                                      |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.5 ms: 1.30x faster                                                      |
| float          | 48.1 ms                                                     | 44.3 ms: 1.09x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_dna      | 114 ms                                                      | 116 ms: 1.01x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 16.1 ms: 1.10x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 95.0 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 53.3 ms                                                     | 49.4 ms: 1.08x faster                                                      |
| tomli_loads          | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| pickle_list          | 2.89 us                                                     | 2.76 us: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.4 ms: 1.03x faster                                                      |
| pickle_dict          | 18.0 us                                                     | 17.6 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 60.9 ms: 1.02x faster                                                      |
| pickle               | 7.34 us                                                     | 7.19 us: 1.02x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 5.87 ms: 1.02x slower                                                      |
| unpickle             | 8.63 us                                                     | 8.89 us: 1.03x slower                                                      |
| unpickle_list        | 2.72 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 191 us: 1.04x slower                                                       |
| unpickle_pure_python | 127 us                                                      | 142 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.3 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.21 ms: 1.20x faster                                                      |
| django_template | 21.8 ms                                                     | 26.9 ms: 1.24x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.8 ms: 1.26x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 44.1 ms: 1.34x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 513 us: 16.91x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 15.5 us: 1.41x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 480 ms: 1.36x faster                                                       |
| spectral_norm              | 59.2 ms                                                     | 44.1 ms: 1.34x faster                                                      |
| nbody                      | 64.5 ms                                                     | 49.5 ms: 1.30x faster                                                      |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                       |
| mako                       | 6.24 ms                                                     | 5.21 ms: 1.20x faster                                                      |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.37 sec: 1.19x faster                                                     |
| scimark_sor                | 72.0 ms                                                     | 61.2 ms: 1.18x faster                                                      |
| scimark_fft                | 174 ms                                                      | 150 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 256 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.09 ms: 1.12x faster                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 38.7 ms: 1.11x faster                                                      |
| float                      | 48.1 ms                                                     | 44.3 ms: 1.09x faster                                                      |
| async_tree_none            | 223 ms                                                      | 206 ms: 1.09x faster                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 49.4 ms: 1.08x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.07x faster                                                      |
| pycparser                  | 758 ms                                                      | 709 ms: 1.07x faster                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| pathlib                    | 81.2 ms                                                     | 76.1 ms: 1.07x faster                                                      |
| tornado_http               | 92.8 ms                                                     | 87.6 ms: 1.06x faster                                                      |
| pickle_list                | 2.89 us                                                     | 2.76 us: 1.05x faster                                                      |
| async_tree_memoization     | 271 ms                                                      | 260 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 198 ms: 1.04x faster                                                       |
| pyflate                    | 275 ms                                                      | 265 ms: 1.04x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 35.4 ms: 1.03x faster                                                      |
| deltablue                  | 1.86 ms                                                     | 1.81 ms: 1.03x faster                                                      |
| fannkuch                   | 245 ms                                                      | 238 ms: 1.03x faster                                                       |
| bench_thread_pool          | 828 us                                                      | 803 us: 1.03x faster                                                       |
| pickle_dict                | 18.0 us                                                     | 17.6 us: 1.03x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.73 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 60.9 ms: 1.02x faster                                                      |
| pickle                     | 7.34 us                                                     | 7.19 us: 1.02x faster                                                      |
| json                       | 2.98 ms                                                     | 2.94 ms: 1.02x faster                                                      |
| coverage                   | 46.7 ms                                                     | 46.1 ms: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.54 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.60 us: 1.00x slower                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| regex_dna                  | 114 ms                                                      | 116 ms: 1.01x slower                                                       |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 73.5 ms: 1.02x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.41 sec: 1.02x slower                                                     |
| json_dumps                 | 5.76 ms                                                     | 5.87 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 395 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 503 ms: 1.02x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.3 ms: 1.03x slower                                                      |
| unpickle                   | 8.63 us                                                     | 8.89 us: 1.03x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 71.7 ms: 1.03x slower                                                      |
| comprehensions             | 10.2 us                                                     | 10.6 us: 1.03x slower                                                      |
| unpickle_list              | 2.72 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 191 us: 1.04x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.04 sec: 1.05x slower                                                     |
| chaos                      | 37.9 ms                                                     | 40.0 ms: 1.06x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.04 us: 1.06x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 42.6 ms: 1.06x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.52 us: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 397 ms: 1.06x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 42.9 ms: 1.07x slower                                                      |
| go                         | 84.6 ms                                                     | 91.3 ms: 1.08x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 41.9 ms: 1.08x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 899 us: 1.09x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 562 ms: 1.10x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 16.1 ms: 1.10x slower                                                      |
| 2to3                       | 217 ms                                                      | 241 ms: 1.11x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 56.7 ns: 1.11x slower                                                      |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 127 us                                                      | 142 us: 1.12x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 62.4 ms: 1.12x slower                                                      |
| sympy_str                  | 166 ms                                                      | 188 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 114 us: 1.13x slower                                                       |
| sympy_sum                  | 86.4 ms                                                     | 98.3 ms: 1.14x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 880 us: 1.16x slower                                                       |
| sympy_expand               | 285 ms                                                      | 330 ms: 1.16x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.16x slower                                                      |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 201 ms: 1.17x slower                                                       |
| generators                 | 19.5 ms                                                     | 23.1 ms: 1.18x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 95.0 ms: 1.19x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.8 ms: 1.20x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.15 ms: 1.21x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                                     |
| sqlglot_optimize           | 33.1 ms                                                     | 40.3 ms: 1.22x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.9 ms: 1.24x slower                                                      |
| pylint                     | 211 ms                                                      | 264 ms: 1.25x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 18.8 ms: 1.26x slower                                                      |
| raytrace                   | 156 ms                                                      | 197 ms: 1.26x slower                                                       |
| richards_super             | 29.3 ms                                                     | 38.6 ms: 1.32x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.87 ms: 1.32x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 44.1 ms: 1.34x slower                                                      |
| richards                   | 26.0 ms                                                     | 36.1 ms: 1.39x slower                                                      |
| unpack_sequence            | 40.0 ns                                                     | 58.0 ns: 1.45x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (3): python_startup, scimark_lu, xml_etree_parse
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 99.31% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown