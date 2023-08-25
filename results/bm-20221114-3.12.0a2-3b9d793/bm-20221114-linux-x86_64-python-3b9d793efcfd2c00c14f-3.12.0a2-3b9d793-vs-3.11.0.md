
# Results vs. 3.11.0

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: linux-x86_64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 245 ms: 1.06x faster                                                  |
| chameleon      | 6.47 ms                                                | 6.30 ms: 1.03x faster                                                 |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                |
| html5lib       | 64.5 ms                                                | 58.9 ms: 1.09x faster                                                 |
| tornado_http   | 96.3 ms                                                | 93.1 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.0 ms: 1.07x faster                                                 |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| nbody          | 93.1 ms                                                | 93.9 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.47 ms: 1.15x faster                                                 |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                                  |
| regex_v8       | 22.0 ms                                                | 21.1 ms: 1.05x faster                                                 |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.66 ms: 1.30x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                                  |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                 |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                  |
| unpickle             | 13.7 us                                                | 12.9 us: 1.06x faster                                                 |
| pickle               | 10.1 us                                                | 9.88 us: 1.02x faster                                                 |
| pickle_list          | 4.11 us                                                | 4.06 us: 1.01x faster                                                 |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                 |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.58 ms: 1.01x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.12 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                 |
| mako            | 10.1 ms                                                | 9.39 ms: 1.07x faster                                                 |
| genshi_text     | 21.6 ms                                                | 20.2 ms: 1.07x faster                                                 |
| django_template | 32.6 ms                                                | 32.8 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.66 ms: 1.30x faster                                                 |
| mypy2                   | 420 ms                                                 | 325 ms: 1.29x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.47 ms: 1.15x faster                                                 |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.00 ms: 1.13x faster                                                 |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.12x faster                                                  |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                 |
| genshi_xml              | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                 |
| aiohttp                 | 1.10 ms                                                | 999 us: 1.10x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 33.6 us: 1.10x faster                                                 |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.10x faster                                                |
| html5lib                | 64.5 ms                                                | 58.9 ms: 1.09x faster                                                 |
| richards                | 45.7 ms                                                | 41.8 ms: 1.09x faster                                                 |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                 |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                                  |
| logging_silent          | 101 ns                                                 | 93.4 ns: 1.08x faster                                                 |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                  |
| mako                    | 10.1 ms                                                | 9.39 ms: 1.07x faster                                                 |
| raytrace                | 297 ms                                                 | 277 ms: 1.07x faster                                                  |
| float                   | 77.2 ms                                                | 72.0 ms: 1.07x faster                                                 |
| genshi_text             | 21.6 ms                                                | 20.2 ms: 1.07x faster                                                 |
| gc_traversal            | 4.02 ms                                                | 3.77 ms: 1.07x faster                                                 |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                  |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                                  |
| json                    | 4.94 ms                                                | 4.65 ms: 1.06x faster                                                 |
| logging_format          | 6.68 us                                                | 6.30 us: 1.06x faster                                                 |
| logging_simple          | 6.03 us                                                | 5.70 us: 1.06x faster                                                 |
| unpickle                | 13.7 us                                                | 12.9 us: 1.06x faster                                                 |
| 2to3                    | 259 ms                                                 | 245 ms: 1.06x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.04 ms: 1.06x faster                                                 |
| spectral_norm           | 100 ms                                                 | 94.9 ms: 1.05x faster                                                 |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.05x faster                                                |
| sqlglot_transpile       | 1.70 ms                                                | 1.62 ms: 1.05x faster                                                 |
| sqlglot_parse           | 1.40 ms                                                | 1.33 ms: 1.05x faster                                                 |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                                  |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                |
| chaos                   | 69.2 ms                                                | 65.8 ms: 1.05x faster                                                 |
| bench_thread_pool       | 819 us                                                 | 780 us: 1.05x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.05x faster                                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| regex_v8                | 22.0 ms                                                | 21.1 ms: 1.05x faster                                                 |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 884 ms: 1.04x faster                                                  |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                 |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                  |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                                  |
| async_generators        | 368 ms                                                 | 355 ms: 1.04x faster                                                  |
| tornado_http            | 96.3 ms                                                | 93.1 ms: 1.03x faster                                                 |
| telco                   | 6.58 ms                                                | 6.38 ms: 1.03x faster                                                 |
| coroutines              | 25.5 ms                                                | 24.7 ms: 1.03x faster                                                 |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                 |
| dulwich_log             | 63.7 ms                                                | 61.8 ms: 1.03x faster                                                 |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                  |
| nqueens                 | 83.4 ms                                                | 81.1 ms: 1.03x faster                                                 |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                 |
| chameleon               | 6.47 ms                                                | 6.30 ms: 1.03x faster                                                 |
| pprint_safe_repr        | 701 ms                                                 | 685 ms: 1.02x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                 |
| pickle                  | 10.1 us                                                | 9.88 us: 1.02x faster                                                 |
| deepcopy_reduce         | 2.94 us                                                | 2.89 us: 1.02x faster                                                 |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 730 ms: 1.01x faster                                                  |
| pickle_list             | 4.11 us                                                | 4.06 us: 1.01x faster                                                 |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                 |
| thrift                  | 756 us                                                 | 748 us: 1.01x faster                                                  |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| django_template         | 32.6 ms                                                | 32.8 ms: 1.01x slower                                                 |
| python_startup          | 8.52 ms                                                | 8.58 ms: 1.01x slower                                                 |
| nbody                   | 93.1 ms                                                | 93.9 ms: 1.01x slower                                                 |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                 |
| unpickle_list           | 4.91 us                                                | 4.98 us: 1.01x slower                                                 |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                |
| python_startup_no_site  | 6.01 ms                                                | 6.12 ms: 1.02x slower                                                 |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                 |
| async_tree_memoization  | 627 ms                                                 | 653 ms: 1.04x slower                                                  |
| comprehensions          | 22.4 us                                                | 23.4 us: 1.04x slower                                                 |
| generators              | 73.5 ms                                                | 77.4 ms: 1.05x slower                                                 |
| unpack_sequence         | 43.1 ns                                                | 45.7 ns: 1.06x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (8): crypto_pyaes, scimark_monte_carlo, bench_mp_pool, xml_etree_process, dask, djangocms, async_tree_none, coverage
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
