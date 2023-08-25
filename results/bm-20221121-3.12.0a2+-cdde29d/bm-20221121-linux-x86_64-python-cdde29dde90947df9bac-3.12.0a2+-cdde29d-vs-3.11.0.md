
# Results vs. 3.11.0

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 244 ms: 1.06x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.31 ms: 1.03x faster                                                  |
| docutils       | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                 |
| html5lib       | 64.5 ms                                                | 59.1 ms: 1.09x faster                                                  |
| tornado_http   | 96.3 ms                                                | 92.8 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.1 ms: 1.06x faster                                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.55 ms: 1.13x faster                                                  |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.0 ms: 1.05x faster                                                  |
| regex_dna      | 204 ms                                                 | 209 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                   |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| pickle_list          | 4.11 us                                                | 3.97 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| xml_etree_process    | 53.9 ms                                                | 52.8 ms: 1.02x faster                                                  |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.01x slower                                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.13 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (2): unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.48 ms: 1.01x faster                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.12 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                  |
| genshi_text     | 21.6 ms                                                | 20.2 ms: 1.07x faster                                                  |
| mako            | 10.1 ms                                                | 9.56 ms: 1.06x faster                                                  |
| django_template | 32.6 ms                                                | 32.1 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.17 ms: 1.16x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.55 ms: 1.13x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                  |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 991 us: 1.11x faster                                                   |
| richards                | 45.7 ms                                                | 41.3 ms: 1.11x faster                                                  |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                   |
| pycparser               | 1.18 sec                                               | 1.07 sec: 1.11x faster                                                 |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.08 ms: 1.10x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 33.8 us: 1.10x faster                                                  |
| html5lib                | 64.5 ms                                                | 59.1 ms: 1.09x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                                   |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                   |
| logging_silent          | 101 ns                                                 | 94.1 ns: 1.07x faster                                                  |
| logging_simple          | 6.03 us                                                | 5.62 us: 1.07x faster                                                  |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                                  |
| scimark_fft             | 328 ms                                                 | 307 ms: 1.07x faster                                                   |
| genshi_text             | 21.6 ms                                                | 20.2 ms: 1.07x faster                                                  |
| logging_format          | 6.68 us                                                | 6.29 us: 1.06x faster                                                  |
| docutils                | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                 |
| 2to3                    | 259 ms                                                 | 244 ms: 1.06x faster                                                   |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.2 ms: 1.06x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 774 us: 1.06x faster                                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.32 ms: 1.06x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.61 ms: 1.06x faster                                                  |
| float                   | 77.2 ms                                                | 73.1 ms: 1.06x faster                                                  |
| mako                    | 10.1 ms                                                | 9.56 ms: 1.06x faster                                                  |
| chaos                   | 69.2 ms                                                | 65.6 ms: 1.05x faster                                                  |
| pyflate                 | 418 ms                                                 | 397 ms: 1.05x faster                                                   |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| regex_v8                | 22.0 ms                                                | 21.0 ms: 1.05x faster                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 65.0 ms: 1.05x faster                                                  |
| spectral_norm           | 100 ms                                                 | 95.6 ms: 1.05x faster                                                  |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                   |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.05x faster                                                   |
| coroutines              | 25.5 ms                                                | 24.5 ms: 1.04x faster                                                  |
| fannkuch                | 388 ms                                                 | 373 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 676 ms: 1.04x faster                                                   |
| tornado_http            | 96.3 ms                                                | 92.8 ms: 1.04x faster                                                  |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                   |
| pickle_list             | 4.11 us                                                | 3.97 us: 1.04x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 61.5 ms: 1.04x faster                                                  |
| sympy_str               | 290 ms                                                 | 280 ms: 1.03x faster                                                   |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.18 ms: 1.03x faster                                                  |
| async_generators        | 368 ms                                                 | 358 ms: 1.03x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.31 ms: 1.03x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                  |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| telco                   | 6.58 ms                                                | 6.44 ms: 1.02x faster                                                  |
| xml_etree_process       | 53.9 ms                                                | 52.8 ms: 1.02x faster                                                  |
| nqueens                 | 83.4 ms                                                | 82.0 ms: 1.02x faster                                                  |
| django_template         | 32.6 ms                                                | 32.1 ms: 1.02x faster                                                  |
| thrift                  | 756 us                                                 | 748 us: 1.01x faster                                                   |
| python_startup          | 8.52 ms                                                | 8.48 ms: 1.01x faster                                                  |
| pickle_dict             | 31.1 us                                                | 31.3 us: 1.01x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.99 us: 1.02x slower                                                  |
| coverage                | 100 ms                                                 | 102 ms: 1.02x slower                                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.12 ms: 1.02x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| async_tree_cpu_io_mixed | 739 ms                                                 | 755 ms: 1.02x slower                                                   |
| regex_dna               | 204 ms                                                 | 209 ms: 1.03x slower                                                   |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                  |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.03x slower                                                 |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.13 us: 1.04x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 45.1 ns: 1.05x slower                                                  |
| generators              | 73.5 ms                                                | 77.7 ms: 1.06x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (7): async_tree_memoization, unpickle, bench_mp_pool, xml_etree_generate, crypto_pyaes, nbody, async_tree_none
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221121-3.12.0a2+-cdde29d/bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
