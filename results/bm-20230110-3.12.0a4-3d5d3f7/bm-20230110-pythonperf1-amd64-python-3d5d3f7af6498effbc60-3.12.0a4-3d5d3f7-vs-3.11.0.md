
# Results vs. 3.11.0

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: windows-amd64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.12x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 193 ms: 1.08x faster                                                       |
| chameleon      | 5.11 ms                                                     | 4.39 ms: 1.17x faster                                                      |
| docutils       | 1.60 sec                                                    | 1.48 sec: 1.08x faster                                                     |
| html5lib       | 37.5 ms                                                     | 33.7 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 59.5 ms: 1.18x faster                                                      |
| float          | 54.6 ms                                                     | 47.2 ms: 1.16x faster                                                      |
| pidigits       | 148 ms                                                      | 145 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 78.8 ms: 1.15x faster                                                      |
| regex_v8       | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.10 ms: 1.48x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 119 us: 1.27x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 169 us: 1.18x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 86.5 ms: 1.11x faster                                                      |
| xml_etree_process    | 37.1 ms                                                     | 33.8 ms: 1.10x faster                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 48.3 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.1 ms: 1.04x faster                                                      |
| json_loads           | 12.9 us                                                     | 12.4 us: 1.04x faster                                                      |
| unpickle_list        | 2.55 us                                                     | 2.59 us: 1.02x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.81 us: 1.05x slower                                                      |
| unpickle             | 8.09 us                                                     | 8.70 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (2): pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.2 ms: 1.04x faster                                                      |
| python_startup         | 18.7 ms                                                     | 18.1 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.3 ms: 1.28x faster                                                      |
| genshi_xml      | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                                      |
| mako            | 7.26 ms                                                     | 6.05 ms: 1.20x faster                                                      |
| django_template | 24.1 ms                                                     | 20.7 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.2 ns: 1.76x faster                                                      |
| asyncio_tcp             | 699 ms                                                      | 466 ms: 1.50x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.10 ms: 1.48x faster                                                      |
| deltablue               | 2.61 ms                                                     | 1.94 ms: 1.34x faster                                                      |
| logging_silent          | 69.8 ns                                                     | 54.2 ns: 1.29x faster                                                      |
| genshi_text             | 17.0 ms                                                     | 13.3 ms: 1.28x faster                                                      |
| richards                | 30.6 ms                                                     | 24.0 ms: 1.27x faster                                                      |
| unpickle_pure_python    | 152 us                                                      | 119 us: 1.27x faster                                                       |
| json                    | 3.25 ms                                                     | 2.61 ms: 1.25x faster                                                      |
| deepcopy_memo           | 25.2 us                                                     | 20.4 us: 1.24x faster                                                      |
| raytrace                | 211 ms                                                      | 171 ms: 1.23x faster                                                       |
| deepcopy                | 246 us                                                      | 199 us: 1.23x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                                      |
| go                      | 97.3 ms                                                     | 80.4 ms: 1.21x faster                                                      |
| hexiom                  | 4.55 ms                                                     | 3.77 ms: 1.21x faster                                                      |
| mako                    | 7.26 ms                                                     | 6.05 ms: 1.20x faster                                                      |
| scimark_sor             | 75.6 ms                                                     | 63.7 ms: 1.19x faster                                                      |
| pickle_pure_python      | 200 us                                                      | 169 us: 1.18x faster                                                       |
| nbody                   | 70.0 ms                                                     | 59.5 ms: 1.18x faster                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 38.0 ms: 1.17x faster                                                      |
| django_template         | 24.1 ms                                                     | 20.7 ms: 1.17x faster                                                      |
| chameleon               | 5.11 ms                                                     | 4.39 ms: 1.17x faster                                                      |
| fannkuch                | 252 ms                                                      | 217 ms: 1.16x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.78 us: 1.16x faster                                                      |
| float                   | 54.6 ms                                                     | 47.2 ms: 1.16x faster                                                      |
| pyflate                 | 304 ms                                                      | 263 ms: 1.15x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 78.8 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.25 ms: 1.14x faster                                                      |
| pprint_safe_repr        | 512 ms                                                      | 448 ms: 1.14x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.02 ms: 1.14x faster                                                      |
| sqlglot_optimize        | 34.9 ms                                                     | 30.6 ms: 1.14x faster                                                      |
| scimark_lu              | 63.5 ms                                                     | 56.0 ms: 1.13x faster                                                      |
| logging_simple          | 6.61 us                                                     | 5.84 us: 1.13x faster                                                      |
| nqueens                 | 64.9 ms                                                     | 57.3 ms: 1.13x faster                                                      |
| pprint_pformat          | 1.04 sec                                                    | 918 ms: 1.13x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 168 ms: 1.13x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 848 us: 1.12x faster                                                       |
| chaos                   | 47.1 ms                                                     | 42.1 ms: 1.12x faster                                                      |
| logging_format          | 7.01 us                                                     | 6.29 us: 1.11x faster                                                      |
| html5lib                | 37.5 ms                                                     | 33.7 ms: 1.11x faster                                                      |
| dulwich_log             | 44.5 ms                                                     | 40.1 ms: 1.11x faster                                                      |
| xml_etree_parse         | 95.9 ms                                                     | 86.5 ms: 1.11x faster                                                      |
| mdp                     | 1.67 sec                                                    | 1.51 sec: 1.10x faster                                                     |
| pycparser               | 691 ms                                                      | 628 ms: 1.10x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 67.9 ms: 1.10x faster                                                      |
| sympy_integrate         | 13.8 ms                                                     | 12.6 ms: 1.10x faster                                                      |
| sympy_expand            | 295 ms                                                      | 269 ms: 1.10x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 33.8 ms: 1.10x faster                                                      |
| mypy2                   | 229 ms                                                      | 209 ms: 1.10x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.59 ms: 1.09x faster                                                      |
| async_tree_memoization  | 371 ms                                                      | 342 ms: 1.09x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 92.0 ms: 1.09x faster                                                      |
| async_tree_none         | 320 ms                                                      | 295 ms: 1.09x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.48 sec: 1.08x faster                                                     |
| spectral_norm           | 67.9 ms                                                     | 62.8 ms: 1.08x faster                                                      |
| 2to3                    | 209 ms                                                      | 193 ms: 1.08x faster                                                       |
| sympy_str               | 182 ms                                                      | 168 ms: 1.08x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 48.3 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed | 501 ms                                                      | 465 ms: 1.08x faster                                                       |
| dask                    | 264 ms                                                      | 246 ms: 1.08x faster                                                       |
| scimark_fft             | 178 ms                                                      | 167 ms: 1.07x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 798 us: 1.07x faster                                                       |
| coverage                | 55.9 ms                                                     | 52.5 ms: 1.06x faster                                                      |
| comprehensions          | 15.9 us                                                     | 15.0 us: 1.06x faster                                                      |
| thrift                  | 491 us                                                      | 463 us: 1.06x faster                                                       |
| coroutines              | 14.6 ms                                                     | 13.9 ms: 1.05x faster                                                      |
| async_generators        | 178 ms                                                      | 169 ms: 1.05x faster                                                       |
| async_tree_io           | 779 ms                                                      | 742 ms: 1.05x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 661 us: 1.05x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.2 ms: 1.04x faster                                                      |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.1 ms: 1.04x faster                                                      |
| crypto_pyaes            | 47.6 ms                                                     | 45.9 ms: 1.04x faster                                                      |
| json_loads              | 12.9 us                                                     | 12.4 us: 1.04x faster                                                      |
| python_startup          | 18.7 ms                                                     | 18.1 ms: 1.03x faster                                                      |
| bench_mp_pool           | 62.5 ms                                                     | 61.1 ms: 1.02x faster                                                      |
| generators              | 33.8 ms                                                     | 33.1 ms: 1.02x faster                                                      |
| pidigits                | 148 ms                                                      | 145 ms: 1.02x faster                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.43 ms: 1.02x faster                                                      |
| regex_v8                | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                      |
| unpickle_list           | 2.55 us                                                     | 2.59 us: 1.02x slower                                                      |
| sqlite_synth            | 1.68 us                                                     | 1.72 us: 1.02x slower                                                      |
| pathlib                 | 71.4 ms                                                     | 73.2 ms: 1.03x slower                                                      |
| regex_dna               | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.81 us: 1.05x slower                                                      |
| regex_effbot            | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                                      |
| unpickle                | 8.09 us                                                     | 8.70 us: 1.07x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (2): pickle_dict, pickle
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.08x
