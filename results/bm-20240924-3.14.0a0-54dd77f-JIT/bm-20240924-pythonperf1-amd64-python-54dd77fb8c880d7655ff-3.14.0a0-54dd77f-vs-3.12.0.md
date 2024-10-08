# Results vs. 3.12.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: windows-amd64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.03x faster
- HPT reliability: 59.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 243 ms: 1.11x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 97.3 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 255 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 555 ms: 1.39x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 392 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                       |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.2 ms: 1.46x faster                                                      |
| float          | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 96.5 ms: 1.10x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 49.9 ms: 1.12x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.7 us: 1.04x faster                                                      |
| pickle               | 7.43 us                                                     | 7.31 us: 1.02x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 198 us: 1.01x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.84 ms: 1.02x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.06x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.16 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.3 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.92 ms: 1.44x faster                                                      |
| django_template | 22.9 ms                                                     | 26.8 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.5 us: 1.53x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 43.8 ms: 1.53x faster                                                      |
| nbody                      | 71.9 ms                                                     | 49.2 ms: 1.46x faster                                                      |
| mako                       | 7.09 ms                                                     | 4.92 ms: 1.44x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 255 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 555 ms: 1.39x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.53 sec: 1.37x faster                                                     |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| float                      | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 61.1 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 392 ms: 1.28x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 38.7 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                       |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                       |
| scimark_fft                | 184 ms                                                      | 148 ms: 1.24x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.84 ms: 1.17x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.20 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.9 ms: 1.12x faster                                                      |
| pyflate                    | 295 ms                                                      | 265 ms: 1.11x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.10x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 806 us: 1.06x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 55.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.97 us: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.41 us: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                      |
| chaos                      | 43.3 ms                                                     | 41.7 ms: 1.04x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.7 us: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.8 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.5 ms: 1.02x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.31 us: 1.02x faster                                                      |
| fannkuch                   | 247 ms                                                      | 243 ms: 1.02x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 62.2 ms: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 75.2 ms: 1.01x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 198 us: 1.01x slower                                                       |
| pathlib                    | 80.5 ms                                                     | 81.6 ms: 1.01x slower                                                      |
| go                         | 91.6 ms                                                     | 93.2 ms: 1.02x slower                                                      |
| generators                 | 22.5 ms                                                     | 22.9 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.84 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 71.5 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 539 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 736 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.06x slower                                                       |
| raytrace                   | 192 ms                                                      | 207 ms: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                     |
| tornado_http               | 89.5 ms                                                     | 97.3 ms: 1.09x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 203 ms: 1.09x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 99.7 ms: 1.09x slower                                                      |
| async_generators           | 239 ms                                                      | 261 ms: 1.09x slower                                                       |
| sympy_str                  | 175 ms                                                      | 192 ms: 1.09x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 96.5 ms: 1.10x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 542 ms: 1.11x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 896 us: 1.11x slower                                                       |
| 2to3                       | 218 ms                                                      | 243 ms: 1.11x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.16 us: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.3 ms: 1.12x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.16 ms: 1.14x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.2 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.14x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.0 ms: 1.16x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.3 ms: 1.16x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                                     |
| django_template            | 22.9 ms                                                     | 26.8 ms: 1.17x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 40.8 ms: 1.18x slower                                                      |
| sympy_expand               | 284 ms                                                      | 337 ms: 1.19x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 895 us: 1.19x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.3 ms: 1.23x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 5.03 ms: 1.23x slower                                                      |
| richards                   | 28.4 ms                                                     | 37.3 ms: 1.31x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 56.3 ns: 1.50x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (3): logging_silent, xml_etree_parse, pickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 59.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown