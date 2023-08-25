
# Results vs. 3.11.0

- fork: faster-cpython
- ref: perf_perf
- machine: linux-x86_64
- commit hash: 2aab3df
- commit date: 2023-03-23
- overall geometric mean: 1.04x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 271 ms: 1.04x slower                                                  |
| chameleon      | 6.47 ms                                                | 7.07 ms: 1.09x slower                                                 |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                |
| html5lib       | 64.5 ms                                                | 68.3 ms: 1.06x slower                                                 |
| tornado_http   | 96.3 ms                                                | 104 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| nbody          | 93.1 ms                                                | 89.0 ms: 1.05x faster                                                 |
| float          | 77.2 ms                                                | 79.0 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.40 ms: 1.17x faster                                                 |
| regex_dna      | 204 ms                                                 | 206 ms: 1.01x slower                                                  |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                 |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.78 ms: 1.29x faster                                                 |
| json_loads           | 26.5 us                                                | 24.4 us: 1.08x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                  |
| pickle_dict          | 31.1 us                                                | 30.5 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                 |
| unpickle_pure_python | 228 us                                                 | 238 us: 1.04x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.20 us: 1.06x slower                                                 |
| pickle_pure_python   | 306 us                                                 | 337 us: 1.10x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.1 ms: 1.10x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 60.6 ms: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.52 ms: 1.12x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.88 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 52.2 ms: 1.01x slower                                                 |
| mako            | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                 |
| genshi_text     | 21.6 ms                                                | 24.5 ms: 1.13x slower                                                 |
| django_template | 32.6 ms                                                | 39.1 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.10x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                                 |
| asyncio_tcp             | 922 ms                                                 | 522 ms: 1.77x faster                                                  |
| json_dumps              | 12.6 ms                                                | 9.78 ms: 1.29x faster                                                 |
| regex_effbot            | 3.99 ms                                                | 3.40 ms: 1.17x faster                                                 |
| mypy2                   | 420 ms                                                 | 378 ms: 1.11x faster                                                  |
| scimark_fft             | 328 ms                                                 | 302 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.14 ms: 1.09x faster                                                 |
| json_loads              | 26.5 us                                                | 24.4 us: 1.08x faster                                                 |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                                 |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| nbody                   | 93.1 ms                                                | 89.0 ms: 1.05x faster                                                 |
| pickle_dict             | 31.1 us                                                | 30.5 us: 1.02x faster                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                  |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.16 ms: 1.02x faster                                                 |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| unpack_sequence         | 43.1 ns                                                | 42.7 ns: 1.01x faster                                                 |
| aiohttp                 | 1.10 ms                                                | 1.09 ms: 1.01x faster                                                 |
| genshi_xml              | 51.8 ms                                                | 52.2 ms: 1.01x slower                                                 |
| regex_dna               | 204 ms                                                 | 206 ms: 1.01x slower                                                  |
| mdp                     | 2.62 sec                                               | 2.65 sec: 1.01x slower                                                |
| nqueens                 | 83.4 ms                                                | 84.6 ms: 1.01x slower                                                 |
| chaos                   | 69.2 ms                                                | 70.3 ms: 1.02x slower                                                 |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                 |
| bench_thread_pool       | 819 us                                                 | 837 us: 1.02x slower                                                  |
| float                   | 77.2 ms                                                | 79.0 ms: 1.02x slower                                                 |
| coverage                | 100 ms                                                 | 103 ms: 1.03x slower                                                  |
| regex_v8                | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                 |
| djangocms               | 32.4 us                                                | 33.4 us: 1.03x slower                                                 |
| docutils                | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                 |
| pathlib                 | 18.2 ms                                                | 19.0 ms: 1.04x slower                                                 |
| unpickle_pure_python    | 228 us                                                 | 238 us: 1.04x slower                                                  |
| 2to3                    | 259 ms                                                 | 271 ms: 1.04x slower                                                  |
| regex_compile           | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| mako                    | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                 |
| sympy_expand            | 475 ms                                                 | 501 ms: 1.06x slower                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 71.9 ms: 1.06x slower                                                 |
| html5lib                | 64.5 ms                                                | 68.3 ms: 1.06x slower                                                 |
| unpickle_list           | 4.91 us                                                | 5.20 us: 1.06x slower                                                 |
| sympy_integrate         | 21.0 ms                                                | 22.4 ms: 1.07x slower                                                 |
| async_tree_io           | 1.30 sec                                               | 1.39 sec: 1.07x slower                                                |
| sympy_str               | 290 ms                                                 | 311 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 793 ms: 1.07x slower                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 148 ms: 1.07x slower                                                  |
| gc_traversal            | 4.02 ms                                                | 4.32 ms: 1.07x slower                                                 |
| scimark_sor             | 118 ms                                                 | 127 ms: 1.07x slower                                                  |
| sympy_sum               | 167 ms                                                 | 179 ms: 1.08x slower                                                  |
| spectral_norm           | 100 ms                                                 | 108 ms: 1.08x slower                                                  |
| tornado_http            | 96.3 ms                                                | 104 ms: 1.08x slower                                                  |
| async_tree_none         | 526 ms                                                 | 568 ms: 1.08x slower                                                  |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.5 ms: 1.09x slower                                                 |
| async_tree_memoization  | 627 ms                                                 | 684 ms: 1.09x slower                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.59 sec: 1.09x slower                                                |
| chameleon               | 6.47 ms                                                | 7.07 ms: 1.09x slower                                                 |
| thrift                  | 756 us                                                 | 830 us: 1.10x slower                                                  |
| pprint_safe_repr        | 701 ms                                                 | 770 ms: 1.10x slower                                                  |
| dulwich_log             | 63.7 ms                                                | 69.9 ms: 1.10x slower                                                 |
| coroutines              | 25.5 ms                                                | 28.0 ms: 1.10x slower                                                 |
| pickle_pure_python      | 306 us                                                 | 337 us: 1.10x slower                                                  |
| deepcopy                | 342 us                                                 | 377 us: 1.10x slower                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 58.5 ms: 1.10x slower                                                 |
| xml_etree_generate      | 76.2 ms                                                | 84.1 ms: 1.10x slower                                                 |
| hexiom                  | 6.37 ms                                                | 7.09 ms: 1.11x slower                                                 |
| deepcopy_memo           | 37.0 us                                                | 41.2 us: 1.11x slower                                                 |
| python_startup          | 8.52 ms                                                | 9.52 ms: 1.12x slower                                                 |
| sqlglot_normalize       | 108 ms                                                 | 121 ms: 1.12x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 60.6 ms: 1.12x slower                                                 |
| genshi_text             | 21.6 ms                                                | 24.5 ms: 1.13x slower                                                 |
| raytrace                | 297 ms                                                 | 337 ms: 1.13x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.35 us: 1.14x slower                                                 |
| pyflate                 | 418 ms                                                 | 478 ms: 1.14x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.88 ms: 1.14x slower                                                 |
| go                      | 140 ms                                                 | 161 ms: 1.15x slower                                                  |
| comprehensions          | 22.4 us                                                | 26.0 us: 1.16x slower                                                 |
| sqlglot_transpile       | 1.70 ms                                                | 1.99 ms: 1.17x slower                                                 |
| async_generators        | 368 ms                                                 | 436 ms: 1.18x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.66 ms: 1.18x slower                                                 |
| richards                | 45.7 ms                                                | 54.6 ms: 1.19x slower                                                 |
| django_template         | 32.6 ms                                                | 39.1 ms: 1.20x slower                                                 |
| deltablue               | 3.67 ms                                                | 4.47 ms: 1.22x slower                                                 |
| logging_format          | 6.68 us                                                | 8.20 us: 1.23x slower                                                 |
| logging_simple          | 6.03 us                                                | 7.48 us: 1.24x slower                                                 |
| logging_silent          | 101 ns                                                 | 130 ns: 1.29x slower                                                  |
| dask                    | 360 ms                                                 | 557 ms: 1.55x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (8): unpickle, fannkuch, pickle_list, create_gc_cycles, telco, bench_mp_pool, pycparser, crypto_pyaes
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x
