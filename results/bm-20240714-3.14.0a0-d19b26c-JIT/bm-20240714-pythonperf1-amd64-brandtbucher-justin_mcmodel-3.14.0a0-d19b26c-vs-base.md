# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-amd64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 231 ms                                                                     | 234 ms: 1.01x slower                                                       |
| docutils       | 1.76 sec                                                                   | 1.78 sec: 1.01x slower                                                     |
| html5lib       | 39.1 ms                                                                    | 41.9 ms: 1.07x slower                                                      |
| tornado_http   | 86.3 ms                                                                    | 85.4 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg | 518 ms                                                                     | 530 ms: 1.02x slower                                                       |
| async_tree_io    | 522 ms                                                                     | 543 ms: 1.04x slower                                                       |
| Geometric mean   | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 52.7 ms                                                                    | 51.1 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                                    | 1.59 ms: 1.01x slower                                                      |
| regex_dna      | 118 ms                                                                     | 120 ms: 1.01x slower                                                       |
| regex_compile  | 89.0 ms                                                                    | 90.2 ms: 1.01x slower                                                      |
| regex_v8       | 18.2 ms                                                                    | 23.9 ms: 1.32x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.08x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.5 us                                                                    | 14.3 us: 1.02x faster                                                      |
| xml_etree_generate   | 52.4 ms                                                                    | 52.8 ms: 1.01x slower                                                      |
| unpickle_pure_python | 132 us                                                                     | 134 us: 1.02x slower                                                       |
| pickle_pure_python   | 176 us                                                                     | 179 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 60.6 ms                                                                    | 62.1 ms: 1.03x slower                                                      |
| tomli_loads          | 1.25 sec                                                                   | 1.28 sec: 1.03x slower                                                     |
| xml_etree_process    | 37.0 ms                                                                    | 38.1 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.4 ms                                                                    | 17.1 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 5.26 ms                                                                    | 5.18 ms: 1.02x faster                                                      |
| genshi_text     | 17.8 ms                                                                    | 18.2 ms: 1.02x slower                                                      |
| django_template | 25.7 ms                                                                    | 26.3 ms: 1.02x slower                                                      |
| genshi_xml      | 43.7 ms                                                                    | 44.8 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody                   | 52.7 ms                                                                    | 51.1 ms: 1.03x faster                                                      |
| json_loads              | 14.5 us                                                                    | 14.3 us: 1.02x faster                                                      |
| python_startup_no_site  | 17.4 ms                                                                    | 17.1 ms: 1.02x faster                                                      |
| mako                    | 5.26 ms                                                                    | 5.18 ms: 1.02x faster                                                      |
| richards                | 31.0 ms                                                                    | 30.6 ms: 1.01x faster                                                      |
| pprint_pformat          | 957 ms                                                                     | 947 ms: 1.01x faster                                                       |
| tornado_http            | 86.3 ms                                                                    | 85.4 ms: 1.01x faster                                                      |
| richards_super          | 35.1 ms                                                                    | 34.8 ms: 1.01x faster                                                      |
| hexiom                  | 4.65 ms                                                                    | 4.61 ms: 1.01x faster                                                      |
| fannkuch                | 226 ms                                                                     | 225 ms: 1.01x faster                                                       |
| crypto_pyaes            | 41.1 ms                                                                    | 40.8 ms: 1.01x faster                                                      |
| pyflate                 | 262 ms                                                                     | 260 ms: 1.01x faster                                                       |
| logging_simple          | 5.77 us                                                                    | 5.80 us: 1.00x slower                                                      |
| mdp                     | 1.45 sec                                                                   | 1.46 sec: 1.01x slower                                                     |
| logging_silent          | 56.9 ns                                                                    | 57.3 ns: 1.01x slower                                                      |
| pathlib                 | 74.3 ms                                                                    | 74.9 ms: 1.01x slower                                                      |
| xml_etree_generate      | 52.4 ms                                                                    | 52.8 ms: 1.01x slower                                                      |
| deepcopy_reduce         | 1.78 us                                                                    | 1.80 us: 1.01x slower                                                      |
| regex_effbot            | 1.58 ms                                                                    | 1.59 ms: 1.01x slower                                                      |
| logging_format          | 6.21 us                                                                    | 6.27 us: 1.01x slower                                                      |
| docutils                | 1.76 sec                                                                   | 1.78 sec: 1.01x slower                                                     |
| 2to3                    | 231 ms                                                                     | 234 ms: 1.01x slower                                                       |
| spectral_norm           | 45.2 ms                                                                    | 45.8 ms: 1.01x slower                                                      |
| bench_thread_pool       | 798 us                                                                     | 808 us: 1.01x slower                                                       |
| regex_dna               | 118 ms                                                                     | 120 ms: 1.01x slower                                                       |
| regex_compile           | 89.0 ms                                                                    | 90.2 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult | 2.14 ms                                                                    | 2.17 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 37.6 ms                                                                    | 38.1 ms: 1.01x slower                                                      |
| sympy_integrate         | 13.8 ms                                                                    | 14.0 ms: 1.01x slower                                                      |
| sqlglot_transpile       | 1.02 ms                                                                    | 1.04 ms: 1.01x slower                                                      |
| chaos                   | 39.3 ms                                                                    | 40.0 ms: 1.02x slower                                                      |
| unpickle_pure_python    | 132 us                                                                     | 134 us: 1.02x slower                                                       |
| sqlglot_parse           | 800 us                                                                     | 815 us: 1.02x slower                                                       |
| genshi_text             | 17.8 ms                                                                    | 18.2 ms: 1.02x slower                                                      |
| pickle_pure_python      | 176 us                                                                     | 179 us: 1.02x slower                                                       |
| sympy_sum               | 92.2 ms                                                                    | 94.0 ms: 1.02x slower                                                      |
| async_tree_io_tg        | 518 ms                                                                     | 530 ms: 1.02x slower                                                       |
| scimark_sor             | 89.5 ms                                                                    | 91.6 ms: 1.02x slower                                                      |
| django_template         | 25.7 ms                                                                    | 26.3 ms: 1.02x slower                                                      |
| xml_etree_iterparse     | 60.6 ms                                                                    | 62.1 ms: 1.03x slower                                                      |
| deepcopy                | 175 us                                                                     | 180 us: 1.03x slower                                                       |
| tomli_loads             | 1.25 sec                                                                   | 1.28 sec: 1.03x slower                                                     |
| genshi_xml              | 43.7 ms                                                                    | 44.8 ms: 1.03x slower                                                      |
| xml_etree_process       | 37.0 ms                                                                    | 38.1 ms: 1.03x slower                                                      |
| sqlglot_normalize       | 188 ms                                                                     | 193 ms: 1.03x slower                                                       |
| sqlglot_optimize        | 35.4 ms                                                                    | 36.4 ms: 1.03x slower                                                      |
| nqueens                 | 60.1 ms                                                                    | 61.9 ms: 1.03x slower                                                      |
| sympy_str               | 178 ms                                                                     | 184 ms: 1.03x slower                                                       |
| sympy_expand            | 308 ms                                                                     | 319 ms: 1.04x slower                                                       |
| coroutines              | 13.7 ms                                                                    | 14.3 ms: 1.04x slower                                                      |
| async_tree_io           | 522 ms                                                                     | 543 ms: 1.04x slower                                                       |
| raytrace                | 178 ms                                                                     | 185 ms: 1.04x slower                                                       |
| go                      | 93.4 ms                                                                    | 97.7 ms: 1.05x slower                                                      |
| coverage                | 46.2 ms                                                                    | 48.5 ms: 1.05x slower                                                      |
| deltablue               | 2.24 ms                                                                    | 2.35 ms: 1.05x slower                                                      |
| scimark_lu              | 73.0 ms                                                                    | 77.0 ms: 1.05x slower                                                      |
| generators              | 23.4 ms                                                                    | 25.0 ms: 1.07x slower                                                      |
| html5lib                | 39.1 ms                                                                    | 41.9 ms: 1.07x slower                                                      |
| telco                   | 4.42 ms                                                                    | 4.95 ms: 1.12x slower                                                      |
| regex_v8                | 18.2 ms                                                                    | 23.9 ms: 1.32x slower                                                      |
| Geometric mean          | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (27): json, python_startup, pycparser, pprint_safe_repr, typing_runtime_protocols, async_tree_cpu_io_mixed, async_generators, bench_mp_pool, comprehensions, create_gc_cycles, pidigits, meteor_contest, async_tree_cpu_io_mixed_tg, float, gc_traversal, scimark_fft, deepcopy_memo, json_dumps, xml_etree_parse, asyncio_tcp, thrift, pylint, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_tcp_ssl, async_tree_memoization

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown