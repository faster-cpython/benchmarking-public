# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.04x faster
- HPT reliability: 96.97%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 241 ms: 1.11x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.92 sec: 1.15x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 87.6 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 256 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 562 ms: 1.37x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.5 ms: 1.45x faster                                                      |
| float          | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 95.0 ms: 1.09x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.1 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 49.4 ms: 1.13x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.4 ms: 1.07x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.05x faster                                                      |
| pickle               | 7.43 us                                                     | 7.19 us: 1.03x faster                                                      |
| pickle_list          | 2.83 us                                                     | 2.76 us: 1.02x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 191 us: 1.02x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.87 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.07x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.89 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.3 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.1 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.21 ms: 1.36x faster                                                      |
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.5 us: 1.53x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.37 sec: 1.53x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 44.1 ms: 1.52x faster                                                      |
| nbody                      | 71.9 ms                                                     | 49.5 ms: 1.45x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 256 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 562 ms: 1.37x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.21 ms: 1.36x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.30x faster                                                       |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 61.2 ms: 1.29x faster                                                      |
| float                      | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.26x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 38.7 ms: 1.25x faster                                                      |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.09 ms: 1.22x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.81 ms: 1.20x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.4 ms: 1.13x faster                                                      |
| pyflate                    | 295 ms                                                      | 265 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.0 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.0 ms: 1.08x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 803 us: 1.07x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.4 ms: 1.07x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.7 ns: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 76.1 ms: 1.06x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                                      |
| fannkuch                   | 247 ms                                                      | 238 ms: 1.04x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.04 us: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.19 us: 1.03x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.52 us: 1.03x faster                                                      |
| pickle_list                | 2.83 us                                                     | 2.76 us: 1.02x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 87.6 ms: 1.02x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 191 us: 1.02x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 503 ms: 1.02x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.9 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.5 ms: 1.01x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 62.4 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.04 sec: 1.00x faster                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.54 ms: 1.01x slower                                                      |
| pycparser                  | 699 ms                                                      | 709 ms: 1.01x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.1 ms: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| raytrace                   | 192 ms                                                      | 197 ms: 1.03x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.87 ms: 1.03x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 71.7 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.07x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 201 ms: 1.07x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 98.3 ms: 1.07x slower                                                      |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.07x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 95.0 ms: 1.09x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.89 us: 1.09x slower                                                      |
| async_generators           | 239 ms                                                      | 261 ms: 1.09x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 880 us: 1.09x slower                                                       |
| 2to3                       | 218 ms                                                      | 241 ms: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.3 ms: 1.12x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.15 ms: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.1 ms: 1.13x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.1 ms: 1.13x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.1 ms: 1.14x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.8 ms: 1.14x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.73 ms: 1.15x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.92 sec: 1.15x slower                                                     |
| sympy_expand               | 284 ms                                                      | 330 ms: 1.16x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 40.3 ms: 1.17x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.87 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 899 us: 1.20x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.6 ms: 1.20x slower                                                      |
| richards                   | 28.4 ms                                                     | 36.1 ms: 1.27x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 58.0 ns: 1.55x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (3): asyncio_tcp, go, xml_etree_parse
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown