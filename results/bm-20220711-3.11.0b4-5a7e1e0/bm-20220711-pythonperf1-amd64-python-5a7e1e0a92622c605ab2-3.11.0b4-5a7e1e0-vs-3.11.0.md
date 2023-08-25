
# Results vs. 3.11.0

- fork: python
- ref: 5a7e1e0a92622c605ab2
- machine: windows-amd64
- commit hash: 5a7e1e0
- commit date: 2022-07-11
- overall geometric mean: 1.01x slower \*
- HPT reliability: 94.77%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 206 ms: 1.02x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.58 sec: 1.02x faster                                                     |
| html5lib       | 37.5 ms                                                     | 38.9 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 68.7 ms: 1.02x faster                                                      |
| pidigits       | 148 ms                                                      | 146 ms: 1.01x faster                                                       |
| float          | 54.6 ms                                                     | 53.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.70 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|--------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle             | 6.61 us                                                     | 6.48 us: 1.02x faster                                                      |
| pickle_list        | 2.68 us                                                     | 2.65 us: 1.01x faster                                                      |
| xml_etree_process  | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                                      |
| pickle_pure_python | 200 us                                                      | 204 us: 1.02x slower                                                       |
| xml_etree_generate | 52.2 ms                                                     | 53.4 ms: 1.02x slower                                                      |
| unpickle           | 8.09 us                                                     | 8.32 us: 1.03x slower                                                      |
| json_dumps         | 7.56 ms                                                     | 7.78 ms: 1.03x slower                                                      |
| json_loads         | 12.9 us                                                     | 14.1 us: 1.09x slower                                                      |
| unpickle_list      | 2.55 us                                                     | 2.80 us: 1.10x slower                                                      |
| Geometric mean     | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_dict, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                      |
| python_startup         | 18.7 ms                                                     | 18.4 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 38.6 ms: 1.03x slower                                                      |
| django_template | 24.1 ms                                                     | 25.0 ms: 1.04x slower                                                      |
| genshi_text     | 17.0 ms                                                     | 17.6 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| aiohttp                 | 899 us                                                      | 860 us: 1.05x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 664 us: 1.04x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 95.8 ms: 1.04x faster                                                      |
| raytrace                | 211 ms                                                      | 204 ms: 1.03x faster                                                       |
| async_tree_io           | 779 ms                                                      | 753 ms: 1.03x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                      |
| coverage                | 55.9 ms                                                     | 54.1 ms: 1.03x faster                                                      |
| regex_v8                | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                      |
| gc_traversal            | 1.46 ms                                                     | 1.41 ms: 1.03x faster                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.13 ms: 1.03x faster                                                      |
| pylint                  | 326 ms                                                      | 318 ms: 1.02x faster                                                       |
| pickle                  | 6.61 us                                                     | 6.48 us: 1.02x faster                                                      |
| nbody                   | 70.0 ms                                                     | 68.7 ms: 1.02x faster                                                      |
| bench_mp_pool           | 62.5 ms                                                     | 61.4 ms: 1.02x faster                                                      |
| python_startup          | 18.7 ms                                                     | 18.4 ms: 1.02x faster                                                      |
| sqlglot_parse           | 952 us                                                      | 936 us: 1.02x faster                                                       |
| 2to3                    | 209 ms                                                      | 206 ms: 1.02x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.58 sec: 1.02x faster                                                     |
| pidigits                | 148 ms                                                      | 146 ms: 1.01x faster                                                       |
| float                   | 54.6 ms                                                     | 53.9 ms: 1.01x faster                                                      |
| scimark_lu              | 63.5 ms                                                     | 62.7 ms: 1.01x faster                                                      |
| sympy_expand            | 295 ms                                                      | 291 ms: 1.01x faster                                                       |
| async_tree_none         | 320 ms                                                      | 317 ms: 1.01x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.7 us: 1.01x faster                                                      |
| pickle_list             | 2.68 us                                                     | 2.65 us: 1.01x faster                                                      |
| regex_dna               | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 44.3 ms: 1.01x faster                                                      |
| sympy_integrate         | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                      |
| dulwich_log             | 44.5 ms                                                     | 44.2 ms: 1.01x faster                                                      |
| pyflate                 | 304 ms                                                      | 306 ms: 1.01x slower                                                       |
| pprint_safe_repr        | 512 ms                                                      | 515 ms: 1.01x slower                                                       |
| deepcopy_memo           | 25.2 us                                                     | 25.3 us: 1.01x slower                                                      |
| bench_thread_pool       | 852 us                                                      | 858 us: 1.01x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.70 us: 1.01x slower                                                      |
| sqlglot_normalize       | 190 ms                                                      | 192 ms: 1.01x slower                                                       |
| logging_simple          | 6.61 us                                                     | 6.68 us: 1.01x slower                                                      |
| coroutines              | 14.6 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| hexiom                  | 4.55 ms                                                     | 4.61 ms: 1.01x slower                                                      |
| pathlib                 | 71.4 ms                                                     | 72.4 ms: 1.01x slower                                                      |
| xml_etree_process       | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                                      |
| pickle_pure_python      | 200 us                                                      | 204 us: 1.02x slower                                                       |
| deltablue               | 2.61 ms                                                     | 2.66 ms: 1.02x slower                                                      |
| dask                    | 264 ms                                                      | 270 ms: 1.02x slower                                                       |
| sqlalchemy_imperative   | 10.2 ms                                                     | 10.4 ms: 1.02x slower                                                      |
| go                      | 97.3 ms                                                     | 99.5 ms: 1.02x slower                                                      |
| pycparser               | 691 ms                                                      | 706 ms: 1.02x slower                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 53.4 ms: 1.02x slower                                                      |
| logging_format          | 7.01 us                                                     | 7.19 us: 1.03x slower                                                      |
| pprint_pformat          | 1.04 sec                                                    | 1.07 sec: 1.03x slower                                                     |
| unpickle                | 8.09 us                                                     | 8.32 us: 1.03x slower                                                      |
| json_dumps              | 7.56 ms                                                     | 7.78 ms: 1.03x slower                                                      |
| telco                   | 3.90 ms                                                     | 4.02 ms: 1.03x slower                                                      |
| genshi_xml              | 37.3 ms                                                     | 38.6 ms: 1.03x slower                                                      |
| chaos                   | 47.1 ms                                                     | 48.7 ms: 1.03x slower                                                      |
| deepcopy_reduce         | 2.07 us                                                     | 2.14 us: 1.03x slower                                                      |
| html5lib                | 37.5 ms                                                     | 38.9 ms: 1.04x slower                                                      |
| logging_silent          | 69.8 ns                                                     | 72.4 ns: 1.04x slower                                                      |
| django_template         | 24.1 ms                                                     | 25.0 ms: 1.04x slower                                                      |
| genshi_text             | 17.0 ms                                                     | 17.6 ms: 1.04x slower                                                      |
| richards                | 30.6 ms                                                     | 31.7 ms: 1.04x slower                                                      |
| scimark_sor             | 75.6 ms                                                     | 78.5 ms: 1.04x slower                                                      |
| sqlalchemy_declarative  | 81.5 ms                                                     | 84.7 ms: 1.04x slower                                                      |
| nqueens                 | 64.9 ms                                                     | 67.6 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.68 ms: 1.04x slower                                                      |
| scimark_fft             | 178 ms                                                      | 186 ms: 1.04x slower                                                       |
| thrift                  | 491 us                                                      | 518 us: 1.06x slower                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 50.6 ms: 1.06x slower                                                      |
| spectral_norm           | 67.9 ms                                                     | 73.7 ms: 1.08x slower                                                      |
| json_loads              | 12.9 us                                                     | 14.1 us: 1.09x slower                                                      |
| unpickle_list           | 2.55 us                                                     | 2.80 us: 1.10x slower                                                      |
| regex_effbot            | 1.50 ms                                                     | 1.70 ms: 1.14x slower                                                      |
| mypy2                   | 229 ms                                                      | 278 ms: 1.21x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (22): asyncio_tcp, unpack_sequence, xml_etree_parse, pickle_dict, mako, fannkuch, sqlglot_optimize, deepcopy, meteor_contest, sympy_str, async_generators, mdp, tornado_http, flaskblogging, unpickle_pure_python, regex_compile, xml_etree_iterparse, generators, chameleon, async_tree_memoization, async_tree_cpu_io_mixed, json
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 94.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
