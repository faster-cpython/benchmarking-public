
# Results vs. 3.11.0

- fork: python
- ref: cdde29dde90947df9bac
- machine: windows-amd64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.08x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 194 ms: 1.08x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.62 ms: 1.11x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.55 sec: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 34.8 ms: 1.08x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 88.1 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 59.0 ms: 1.19x faster                                                       |
| float          | 54.6 ms                                                     | 51.0 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 81.1 ms: 1.12x faster                                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.53 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.35 ms: 1.41x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 131 us: 1.16x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 177 us: 1.13x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 33.6 ms: 1.10x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 48.4 ms: 1.08x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 91.0 ms: 1.05x faster                                                       |
| pickle_list          | 2.68 us                                                     | 2.73 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.0 ms: 1.02x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.64 us: 1.04x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.4 us: 1.05x slower                                                       |
| unpickle             | 8.09 us                                                     | 8.52 us: 1.05x slower                                                       |
| pickle               | 6.61 us                                                     | 7.13 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.9 ms: 1.22x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 32.4 ms: 1.15x faster                                                       |
| django_template | 24.1 ms                                                     | 21.0 ms: 1.15x faster                                                       |
| mako            | 7.26 ms                                                     | 6.38 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.3 ns: 1.75x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.35 ms: 1.41x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.08 ms: 1.26x faster                                                       |
| richards                | 30.6 ms                                                     | 24.8 ms: 1.23x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.9 ms: 1.22x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 57.8 ns: 1.21x faster                                                       |
| nbody                   | 70.0 ms                                                     | 59.0 ms: 1.19x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 21.4 us: 1.18x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.87 ms: 1.18x faster                                                       |
| go                      | 97.3 ms                                                     | 82.9 ms: 1.17x faster                                                       |
| json                    | 3.25 ms                                                     | 2.78 ms: 1.17x faster                                                       |
| deepcopy                | 246 us                                                      | 212 us: 1.16x faster                                                        |
| raytrace                | 211 ms                                                      | 182 ms: 1.16x faster                                                        |
| unpickle_pure_python    | 152 us                                                      | 131 us: 1.16x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 32.4 ms: 1.15x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.01 ms: 1.15x faster                                                       |
| django_template         | 24.1 ms                                                     | 21.0 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.24 ms: 1.15x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 833 us: 1.14x faster                                                        |
| pyflate                 | 304 ms                                                      | 267 ms: 1.14x faster                                                        |
| mako                    | 7.26 ms                                                     | 6.38 ms: 1.14x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 59.7 ms: 1.14x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 57.1 ms: 1.14x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.82 us: 1.14x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 177 us: 1.13x faster                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 31.0 ms: 1.12x faster                                                       |
| fannkuch                | 252 ms                                                      | 225 ms: 1.12x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 81.1 ms: 1.12x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 458 ms: 1.12x faster                                                        |
| chaos                   | 47.1 ms                                                     | 42.2 ms: 1.12x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 934 ms: 1.11x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.62 ms: 1.11x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 33.6 ms: 1.10x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.39 us: 1.10x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 174 ms: 1.09x faster                                                        |
| scimark_sor             | 75.6 ms                                                     | 69.5 ms: 1.09x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| dulwich_log             | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 69.2 ms: 1.08x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 58.9 ms: 1.08x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 48.4 ms: 1.08x faster                                                       |
| html5lib                | 37.5 ms                                                     | 34.8 ms: 1.08x faster                                                       |
| 2to3                    | 209 ms                                                      | 194 ms: 1.08x faster                                                        |
| sympy_expand            | 295 ms                                                      | 275 ms: 1.07x faster                                                        |
| float                   | 54.6 ms                                                     | 51.0 ms: 1.07x faster                                                       |
| mypy2                   | 229 ms                                                      | 216 ms: 1.06x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.24 us: 1.06x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.0 ms: 1.06x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.1 us: 1.06x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 42.3 ms: 1.06x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 91.0 ms: 1.05x faster                                                       |
| sympy_str               | 182 ms                                                      | 173 ms: 1.05x faster                                                        |
| coverage                | 55.9 ms                                                     | 53.2 ms: 1.05x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 95.2 ms: 1.05x faster                                                       |
| tornado_http            | 91.8 ms                                                     | 88.1 ms: 1.04x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 45.7 ms: 1.04x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.75 ms: 1.04x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.55 sec: 1.03x faster                                                      |
| dask                    | 264 ms                                                      | 257 ms: 1.03x faster                                                        |
| thrift                  | 491 us                                                      | 478 us: 1.03x faster                                                        |
| async_tree_memoization  | 371 ms                                                      | 363 ms: 1.02x faster                                                        |
| async_tree_none         | 320 ms                                                      | 314 ms: 1.02x faster                                                        |
| scimark_fft             | 178 ms                                                      | 175 ms: 1.02x faster                                                        |
| coroutines              | 14.6 ms                                                     | 14.5 ms: 1.01x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 842 us: 1.01x faster                                                        |
| create_gc_cycles        | 693 us                                                      | 685 us: 1.01x faster                                                        |
| async_generators        | 178 ms                                                      | 176 ms: 1.01x faster                                                        |
| bench_mp_pool           | 62.5 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| generators              | 33.8 ms                                                     | 34.4 ms: 1.02x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.48 ms: 1.02x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.73 us: 1.02x slower                                                       |
| regex_dna               | 115 ms                                                      | 118 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 64.0 ms: 1.02x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.53 ms: 1.03x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.64 us: 1.04x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.4 us: 1.05x slower                                                       |
| unpickle                | 8.09 us                                                     | 8.52 us: 1.05x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.80 us: 1.07x slower                                                       |
| asyncio_tcp             | 699 ms                                                      | 747 ms: 1.07x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 76.4 ms: 1.07x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.13 us: 1.08x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, python_startup_no_site, pidigits, pycparser, python_startup, regex_v8, json_loads, async_tree_io
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
