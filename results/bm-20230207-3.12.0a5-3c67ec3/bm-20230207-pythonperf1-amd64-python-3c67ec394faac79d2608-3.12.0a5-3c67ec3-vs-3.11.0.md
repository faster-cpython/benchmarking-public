
# Results vs. 3.11.0

- fork: python
- ref: 3c67ec394faac79d2608
- machine: windows-amd64
- commit hash: 3c67ec3
- commit date: 2023-02-07
- overall geometric mean: 1.10x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 192 ms: 1.09x faster                                                       |
| chameleon      | 5.11 ms                                                     | 4.41 ms: 1.16x faster                                                      |
| docutils       | 1.60 sec                                                    | 1.50 sec: 1.07x faster                                                     |
| html5lib       | 37.5 ms                                                     | 34.1 ms: 1.10x faster                                                      |
| tornado_http   | 91.8 ms                                                     | 90.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 59.1 ms: 1.18x faster                                                      |
| float          | 54.6 ms                                                     | 47.3 ms: 1.16x faster                                                      |
| pidigits       | 148 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 78.8 ms: 1.15x faster                                                      |
| regex_v8       | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.68 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.38 ms: 1.40x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 120 us: 1.27x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 166 us: 1.20x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 33.5 ms: 1.11x faster                                                      |
| xml_etree_parse      | 95.9 ms                                                     | 88.5 ms: 1.08x faster                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 49.5 ms: 1.06x faster                                                      |
| pickle_list          | 2.68 us                                                     | 2.70 us: 1.01x slower                                                      |
| pickle               | 6.61 us                                                     | 6.77 us: 1.02x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.65 us: 1.04x slower                                                      |
| json_loads           | 12.9 us                                                     | 14.2 us: 1.10x slower                                                      |
| unpickle             | 8.09 us                                                     | 9.39 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.5 ms: 1.03x faster                                                      |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 24.1 ms                                                     | 20.2 ms: 1.20x faster                                                      |
| genshi_text     | 17.0 ms                                                     | 14.2 ms: 1.19x faster                                                      |
| mako            | 7.26 ms                                                     | 6.15 ms: 1.18x faster                                                      |
| genshi_xml      | 37.3 ms                                                     | 32.6 ms: 1.15x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf1-amd64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 25.6 ns: 1.80x faster                                                      |
| asyncio_tcp             | 699 ms                                                      | 466 ms: 1.50x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.38 ms: 1.40x faster                                                      |
| comprehensions          | 15.9 us                                                     | 11.7 us: 1.36x faster                                                      |
| deltablue               | 2.61 ms                                                     | 1.96 ms: 1.33x faster                                                      |
| richards                | 30.6 ms                                                     | 23.9 ms: 1.28x faster                                                      |
| unpickle_pure_python    | 152 us                                                      | 120 us: 1.27x faster                                                       |
| raytrace                | 211 ms                                                      | 170 ms: 1.24x faster                                                       |
| go                      | 97.3 ms                                                     | 78.8 ms: 1.24x faster                                                      |
| hexiom                  | 4.55 ms                                                     | 3.73 ms: 1.22x faster                                                      |
| pickle_pure_python      | 200 us                                                      | 166 us: 1.20x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 58.1 ns: 1.20x faster                                                      |
| django_template         | 24.1 ms                                                     | 20.2 ms: 1.20x faster                                                      |
| genshi_text             | 17.0 ms                                                     | 14.2 ms: 1.19x faster                                                      |
| deepcopy_memo           | 25.2 us                                                     | 21.1 us: 1.19x faster                                                      |
| chaos                   | 47.1 ms                                                     | 39.6 ms: 1.19x faster                                                      |
| nqueens                 | 64.9 ms                                                     | 54.6 ms: 1.19x faster                                                      |
| fannkuch                | 252 ms                                                      | 213 ms: 1.18x faster                                                       |
| nbody                   | 70.0 ms                                                     | 59.1 ms: 1.18x faster                                                      |
| mako                    | 7.26 ms                                                     | 6.15 ms: 1.18x faster                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.18 ms: 1.18x faster                                                      |
| scimark_monte_carlo     | 44.6 ms                                                     | 37.9 ms: 1.18x faster                                                      |
| deepcopy                | 246 us                                                      | 211 us: 1.16x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.41 ms: 1.16x faster                                                      |
| json                    | 3.25 ms                                                     | 2.81 ms: 1.16x faster                                                      |
| float                   | 54.6 ms                                                     | 47.3 ms: 1.16x faster                                                      |
| regex_compile           | 90.6 ms                                                     | 78.8 ms: 1.15x faster                                                      |
| pprint_safe_repr        | 512 ms                                                      | 445 ms: 1.15x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 32.6 ms: 1.15x faster                                                      |
| pprint_pformat          | 1.04 sec                                                    | 907 ms: 1.15x faster                                                       |
| pyflate                 | 304 ms                                                      | 267 ms: 1.14x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 67.0 ms: 1.13x faster                                                      |
| mdp                     | 1.67 sec                                                    | 1.48 sec: 1.13x faster                                                     |
| sqlglot_parse           | 952 us                                                      | 851 us: 1.12x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.28 us: 1.12x faster                                                      |
| sympy_sum               | 99.9 ms                                                     | 89.5 ms: 1.12x faster                                                      |
| sqlglot_normalize       | 190 ms                                                      | 171 ms: 1.12x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.4 ms: 1.11x faster                                                      |
| sympy_str               | 182 ms                                                      | 164 ms: 1.11x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.05 ms: 1.11x faster                                                      |
| xml_etree_process       | 37.1 ms                                                     | 33.5 ms: 1.11x faster                                                      |
| spectral_norm           | 67.9 ms                                                     | 61.5 ms: 1.11x faster                                                      |
| deepcopy_reduce         | 2.07 us                                                     | 1.88 us: 1.10x faster                                                      |
| sqlglot_optimize        | 34.9 ms                                                     | 31.6 ms: 1.10x faster                                                      |
| logging_simple          | 6.61 us                                                     | 6.01 us: 1.10x faster                                                      |
| mypy2                   | 229 ms                                                      | 208 ms: 1.10x faster                                                       |
| html5lib                | 37.5 ms                                                     | 34.1 ms: 1.10x faster                                                      |
| sympy_expand            | 295 ms                                                      | 269 ms: 1.10x faster                                                       |
| pycparser               | 691 ms                                                      | 633 ms: 1.09x faster                                                       |
| 2to3                    | 209 ms                                                      | 192 ms: 1.09x faster                                                       |
| thrift                  | 491 us                                                      | 452 us: 1.08x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 88.5 ms: 1.08x faster                                                      |
| scimark_lu              | 63.5 ms                                                     | 58.7 ms: 1.08x faster                                                      |
| meteor_contest          | 74.7 ms                                                     | 69.1 ms: 1.08x faster                                                      |
| crypto_pyaes            | 47.6 ms                                                     | 44.0 ms: 1.08x faster                                                      |
| coverage                | 55.9 ms                                                     | 51.8 ms: 1.08x faster                                                      |
| scimark_fft             | 178 ms                                                      | 166 ms: 1.08x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.50 sec: 1.07x faster                                                     |
| async_generators        | 178 ms                                                      | 167 ms: 1.06x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                      |
| async_tree_none         | 320 ms                                                      | 302 ms: 1.06x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 49.5 ms: 1.06x faster                                                      |
| telco                   | 3.90 ms                                                     | 3.72 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed | 501 ms                                                      | 480 ms: 1.04x faster                                                       |
| async_tree_memoization  | 371 ms                                                      | 356 ms: 1.04x faster                                                       |
| async_tree_io           | 779 ms                                                      | 748 ms: 1.04x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 823 us: 1.04x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.5 ms: 1.03x faster                                                      |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.02x faster                                                      |
| create_gc_cycles        | 693 us                                                      | 676 us: 1.02x faster                                                       |
| generators              | 33.8 ms                                                     | 33.0 ms: 1.02x faster                                                      |
| pidigits                | 148 ms                                                      | 146 ms: 1.02x faster                                                       |
| tornado_http            | 91.8 ms                                                     | 90.5 ms: 1.02x faster                                                      |
| regex_v8                | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                      |
| bench_mp_pool           | 62.5 ms                                                     | 61.7 ms: 1.01x faster                                                      |
| gc_traversal            | 1.46 ms                                                     | 1.45 ms: 1.01x faster                                                      |
| pickle_list             | 2.68 us                                                     | 2.70 us: 1.01x slower                                                      |
| coroutines              | 14.6 ms                                                     | 14.8 ms: 1.01x slower                                                      |
| pickle                  | 6.61 us                                                     | 6.77 us: 1.02x slower                                                      |
| pathlib                 | 71.4 ms                                                     | 73.7 ms: 1.03x slower                                                      |
| unpickle_list           | 2.55 us                                                     | 2.65 us: 1.04x slower                                                      |
| regex_dna               | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.82 us: 1.08x slower                                                      |
| json_loads              | 12.9 us                                                     | 14.2 us: 1.10x slower                                                      |
| regex_effbot            | 1.50 ms                                                     | 1.68 ms: 1.13x slower                                                      |
| unpickle                | 8.09 us                                                     | 9.39 us: 1.16x slower                                                      |
| dask                    | 264 ms                                                      | 349 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_dict
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x
