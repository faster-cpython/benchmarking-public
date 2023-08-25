
# Results vs. 3.11.0

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: windows-amd64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.07x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 193 ms: 1.08x faster                                                       |
| chameleon      | 5.11 ms                                                     | 4.59 ms: 1.11x faster                                                      |
| docutils       | 1.60 sec                                                    | 1.52 sec: 1.06x faster                                                     |
| html5lib       | 37.5 ms                                                     | 36.4 ms: 1.03x faster                                                      |
| tornado_http   | 91.8 ms                                                     | 89.5 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 62.3 ms: 1.12x faster                                                      |
| float          | 54.6 ms                                                     | 48.7 ms: 1.12x faster                                                      |
| pidigits       | 148 ms                                                      | 146 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 82.3 ms: 1.10x faster                                                      |
| regex_v8       | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.70 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.12 ms: 1.48x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 130 us: 1.16x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 180 us: 1.11x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 33.9 ms: 1.09x faster                                                      |
| xml_etree_parse      | 95.9 ms                                                     | 87.6 ms: 1.09x faster                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 49.0 ms: 1.07x faster                                                      |
| pickle_list          | 2.68 us                                                     | 2.62 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                                      |
| json_loads           | 12.9 us                                                     | 13.3 us: 1.03x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.79 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (3): pickle_dict, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                      |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.4 ms: 1.18x faster                                                      |
| mako            | 7.26 ms                                                     | 6.25 ms: 1.16x faster                                                      |
| genshi_xml      | 37.3 ms                                                     | 32.2 ms: 1.16x faster                                                      |
| django_template | 24.1 ms                                                     | 21.6 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 30.8 ns: 1.49x faster                                                      |
| json_dumps              | 7.56 ms                                                     | 5.12 ms: 1.48x faster                                                      |
| json                    | 3.25 ms                                                     | 2.75 ms: 1.18x faster                                                      |
| genshi_text             | 17.0 ms                                                     | 14.4 ms: 1.18x faster                                                      |
| logging_silent          | 69.8 ns                                                     | 59.9 ns: 1.17x faster                                                      |
| deltablue               | 2.61 ms                                                     | 2.24 ms: 1.17x faster                                                      |
| unpickle_pure_python    | 152 us                                                      | 130 us: 1.16x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.25 ms: 1.16x faster                                                      |
| go                      | 97.3 ms                                                     | 84.0 ms: 1.16x faster                                                      |
| genshi_xml              | 37.3 ms                                                     | 32.2 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.25 ms: 1.14x faster                                                      |
| raytrace                | 211 ms                                                      | 184 ms: 1.14x faster                                                       |
| richards                | 30.6 ms                                                     | 26.7 ms: 1.14x faster                                                      |
| hexiom                  | 4.55 ms                                                     | 4.00 ms: 1.14x faster                                                      |
| deepcopy_memo           | 25.2 us                                                     | 22.2 us: 1.13x faster                                                      |
| deepcopy                | 246 us                                                      | 217 us: 1.13x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 57.5 ms: 1.13x faster                                                      |
| nbody                   | 70.0 ms                                                     | 62.3 ms: 1.12x faster                                                      |
| float                   | 54.6 ms                                                     | 48.7 ms: 1.12x faster                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.8 ms: 1.12x faster                                                      |
| pyflate                 | 304 ms                                                      | 272 ms: 1.12x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 458 ms: 1.12x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 56.9 ms: 1.12x faster                                                      |
| django_template         | 24.1 ms                                                     | 21.6 ms: 1.11x faster                                                      |
| chameleon               | 5.11 ms                                                     | 4.59 ms: 1.11x faster                                                      |
| pprint_pformat          | 1.04 sec                                                    | 934 ms: 1.11x faster                                                       |
| fannkuch                | 252 ms                                                      | 227 ms: 1.11x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 180 us: 1.11x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.87 us: 1.11x faster                                                      |
| regex_compile           | 90.6 ms                                                     | 82.3 ms: 1.10x faster                                                      |
| sqlglot_parse           | 952 us                                                      | 865 us: 1.10x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 33.9 ms: 1.09x faster                                                      |
| xml_etree_parse         | 95.9 ms                                                     | 87.6 ms: 1.09x faster                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.06 ms: 1.09x faster                                                      |
| scimark_sor             | 75.6 ms                                                     | 69.2 ms: 1.09x faster                                                      |
| mdp                     | 1.67 sec                                                    | 1.53 sec: 1.09x faster                                                     |
| chaos                   | 47.1 ms                                                     | 43.1 ms: 1.09x faster                                                      |
| sqlglot_normalize       | 190 ms                                                      | 174 ms: 1.09x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.1 ms: 1.09x faster                                                      |
| mypy2                   | 229 ms                                                      | 212 ms: 1.08x faster                                                       |
| 2to3                    | 209 ms                                                      | 193 ms: 1.08x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 69.3 ms: 1.08x faster                                                      |
| spectral_norm           | 67.9 ms                                                     | 63.1 ms: 1.08x faster                                                      |
| coverage                | 55.9 ms                                                     | 52.0 ms: 1.07x faster                                                      |
| sympy_integrate         | 13.8 ms                                                     | 12.9 ms: 1.07x faster                                                      |
| logging_format          | 7.01 us                                                     | 6.56 us: 1.07x faster                                                      |
| xml_etree_generate      | 52.2 ms                                                     | 49.0 ms: 1.07x faster                                                      |
| pycparser               | 691 ms                                                      | 650 ms: 1.06x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.52 sec: 1.06x faster                                                     |
| scimark_fft             | 178 ms                                                      | 170 ms: 1.05x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 45.4 ms: 1.05x faster                                                      |
| logging_simple          | 6.61 us                                                     | 6.31 us: 1.05x faster                                                      |
| sympy_expand            | 295 ms                                                      | 282 ms: 1.05x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 665 us: 1.04x faster                                                       |
| sympy_str               | 182 ms                                                      | 175 ms: 1.04x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 96.1 ms: 1.04x faster                                                      |
| comprehensions          | 15.9 us                                                     | 15.4 us: 1.04x faster                                                      |
| dulwich_log             | 44.5 ms                                                     | 43.1 ms: 1.03x faster                                                      |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                      |
| html5lib                | 37.5 ms                                                     | 36.4 ms: 1.03x faster                                                      |
| async_generators        | 178 ms                                                      | 173 ms: 1.03x faster                                                       |
| tornado_http            | 91.8 ms                                                     | 89.5 ms: 1.03x faster                                                      |
| dask                    | 264 ms                                                      | 258 ms: 1.03x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.02x faster                                                      |
| pickle_list             | 2.68 us                                                     | 2.62 us: 1.02x faster                                                      |
| bench_thread_pool       | 852 us                                                      | 835 us: 1.02x faster                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                                      |
| bench_mp_pool           | 62.5 ms                                                     | 61.2 ms: 1.02x faster                                                      |
| gc_traversal            | 1.46 ms                                                     | 1.44 ms: 1.01x faster                                                      |
| pidigits                | 148 ms                                                      | 146 ms: 1.01x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                                      |
| telco                   | 3.90 ms                                                     | 3.95 ms: 1.01x slower                                                      |
| async_tree_none         | 320 ms                                                      | 325 ms: 1.02x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 72.6 ms: 1.02x slower                                                      |
| sqlite_synth            | 1.68 us                                                     | 1.71 us: 1.02x slower                                                      |
| coroutines              | 14.6 ms                                                     | 15.0 ms: 1.02x slower                                                      |
| json_loads              | 12.9 us                                                     | 13.3 us: 1.03x slower                                                      |
| regex_dna               | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 386 ms: 1.04x slower                                                       |
| generators              | 33.8 ms                                                     | 35.7 ms: 1.06x slower                                                      |
| unpickle_list           | 2.55 us                                                     | 2.79 us: 1.10x slower                                                      |
| regex_effbot            | 1.50 ms                                                     | 1.70 ms: 1.14x slower                                                      |
| thrift                  | 491 us                                                      | 558 us: 1.14x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (6): pickle_dict, pickle, async_tree_io, async_tree_cpu_io_mixed, asyncio_tcp, unpickle
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x
