
# Results vs. 3.11.0

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: windows-amd64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.08x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 196 ms: 1.07x faster                                                       |
| chameleon      | 5.11 ms                                                     | 4.53 ms: 1.13x faster                                                      |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.02x faster                                                     |
| html5lib       | 37.5 ms                                                     | 35.0 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 62.3 ms: 1.12x faster                                                      |
| float          | 54.6 ms                                                     | 50.1 ms: 1.09x faster                                                      |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 82.5 ms: 1.10x faster                                                      |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                      |
| regex_effbot   | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.17 ms: 1.46x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 121 us: 1.25x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 179 us: 1.12x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 90.5 ms: 1.06x faster                                                      |
| xml_etree_process    | 37.1 ms                                                     | 35.0 ms: 1.06x faster                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 49.7 ms: 1.05x faster                                                      |
| unpickle_list        | 2.55 us                                                     | 2.61 us: 1.03x slower                                                      |
| pickle               | 6.61 us                                                     | 6.90 us: 1.04x slower                                                      |
| pickle_dict          | 18.5 us                                                     | 19.4 us: 1.05x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.85 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 18.5 ms: 1.01x faster                                                      |
| python_startup_no_site | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.8 ms: 1.23x faster                                                      |
| mako            | 7.26 ms                                                     | 6.19 ms: 1.17x faster                                                      |
| genshi_xml      | 37.3 ms                                                     | 32.3 ms: 1.16x faster                                                      |
| django_template | 24.1 ms                                                     | 21.4 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf1-amd64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.4 ns: 1.74x faster                                                      |
| json_dumps              | 7.56 ms                                                     | 5.17 ms: 1.46x faster                                                      |
| deltablue               | 2.61 ms                                                     | 2.07 ms: 1.26x faster                                                      |
| unpickle_pure_python    | 152 us                                                      | 121 us: 1.25x faster                                                       |
| richards                | 30.6 ms                                                     | 24.5 ms: 1.25x faster                                                      |
| genshi_text             | 17.0 ms                                                     | 13.8 ms: 1.23x faster                                                      |
| logging_silent          | 69.8 ns                                                     | 57.2 ns: 1.22x faster                                                      |
| json                    | 3.25 ms                                                     | 2.74 ms: 1.19x faster                                                      |
| deepcopy_memo           | 25.2 us                                                     | 21.2 us: 1.19x faster                                                      |
| raytrace                | 211 ms                                                      | 179 ms: 1.18x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.19 ms: 1.17x faster                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| hexiom                  | 4.55 ms                                                     | 3.89 ms: 1.17x faster                                                      |
| scimark_sor             | 75.6 ms                                                     | 64.6 ms: 1.17x faster                                                      |
| scimark_lu              | 63.5 ms                                                     | 54.8 ms: 1.16x faster                                                      |
| genshi_xml              | 37.3 ms                                                     | 32.3 ms: 1.16x faster                                                      |
| pyflate                 | 304 ms                                                      | 264 ms: 1.15x faster                                                       |
| deepcopy                | 246 us                                                      | 214 us: 1.15x faster                                                       |
| go                      | 97.3 ms                                                     | 84.8 ms: 1.15x faster                                                      |
| fannkuch                | 252 ms                                                      | 222 ms: 1.14x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.53 ms: 1.13x faster                                                      |
| django_template         | 24.1 ms                                                     | 21.4 ms: 1.13x faster                                                      |
| nbody                   | 70.0 ms                                                     | 62.3 ms: 1.12x faster                                                      |
| nqueens                 | 64.9 ms                                                     | 57.9 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.30 ms: 1.12x faster                                                      |
| pickle_pure_python      | 200 us                                                      | 179 us: 1.12x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 458 ms: 1.12x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 172 ms: 1.11x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 61.4 ms: 1.11x faster                                                      |
| sqlglot_parse           | 952 us                                                      | 860 us: 1.11x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.88 us: 1.10x faster                                                      |
| regex_compile           | 90.6 ms                                                     | 82.5 ms: 1.10x faster                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                                      |
| pprint_pformat          | 1.04 sec                                                    | 947 ms: 1.10x faster                                                       |
| chaos                   | 47.1 ms                                                     | 43.2 ms: 1.09x faster                                                      |
| float                   | 54.6 ms                                                     | 50.1 ms: 1.09x faster                                                      |
| sqlglot_optimize        | 34.9 ms                                                     | 32.0 ms: 1.09x faster                                                      |
| meteor_contest          | 74.7 ms                                                     | 68.8 ms: 1.09x faster                                                      |
| coverage                | 55.9 ms                                                     | 51.6 ms: 1.08x faster                                                      |
| dulwich_log             | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| html5lib                | 37.5 ms                                                     | 35.0 ms: 1.07x faster                                                      |
| telco                   | 3.90 ms                                                     | 3.64 ms: 1.07x faster                                                      |
| 2to3                    | 209 ms                                                      | 196 ms: 1.07x faster                                                       |
| mypy2                   | 229 ms                                                      | 215 ms: 1.07x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.22 us: 1.06x faster                                                      |
| xml_etree_parse         | 95.9 ms                                                     | 90.5 ms: 1.06x faster                                                      |
| xml_etree_process       | 37.1 ms                                                     | 35.0 ms: 1.06x faster                                                      |
| logging_format          | 7.01 us                                                     | 6.64 us: 1.06x faster                                                      |
| crypto_pyaes            | 47.6 ms                                                     | 45.1 ms: 1.05x faster                                                      |
| sympy_str               | 182 ms                                                      | 173 ms: 1.05x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 49.7 ms: 1.05x faster                                                      |
| thrift                  | 491 us                                                      | 469 us: 1.05x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                                     |
| sympy_integrate         | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                                      |
| sympy_expand            | 295 ms                                                      | 286 ms: 1.03x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.5 us: 1.03x faster                                                      |
| dask                    | 264 ms                                                      | 258 ms: 1.03x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.02x faster                                                     |
| bench_thread_pool       | 852 us                                                      | 837 us: 1.02x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 682 us: 1.02x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.5 ms: 1.01x faster                                                      |
| gc_traversal            | 1.46 ms                                                     | 1.44 ms: 1.01x faster                                                      |
| scimark_fft             | 178 ms                                                      | 177 ms: 1.01x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                      |
| sympy_sum               | 99.9 ms                                                     | 99.0 ms: 1.01x faster                                                      |
| bench_mp_pool           | 62.5 ms                                                     | 62.8 ms: 1.00x slower                                                      |
| async_generators        | 178 ms                                                      | 179 ms: 1.01x slower                                                       |
| regex_v8                | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                      |
| pathlib                 | 71.4 ms                                                     | 72.1 ms: 1.01x slower                                                      |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.61 us: 1.03x slower                                                      |
| sqlite_synth            | 1.68 us                                                     | 1.73 us: 1.03x slower                                                      |
| coroutines              | 14.6 ms                                                     | 15.1 ms: 1.03x slower                                                      |
| regex_effbot            | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                      |
| regex_dna               | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.90 us: 1.04x slower                                                      |
| async_tree_memoization  | 371 ms                                                      | 388 ms: 1.05x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.4 us: 1.05x slower                                                      |
| asyncio_tcp             | 699 ms                                                      | 735 ms: 1.05x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.85 us: 1.06x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (8): unpickle, async_tree_none, xml_etree_iterparse, json_loads, pycparser, async_tree_cpu_io_mixed, async_tree_io, generators
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
