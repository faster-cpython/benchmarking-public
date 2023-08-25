
# Results vs. 3.11.0

- fork: python
- ref: e5bd5ad70d9e549eeb80
- machine: linux-x86_64
- commit hash: e5bd5ad
- commit date: 2023-01-13
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.25 ms: 1.04x faster                                                  |
| docutils       | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                 |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                  |
| tornado_http   | 96.3 ms                                                | 93.2 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.7 ms: 1.08x faster                                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| nbody          | 93.1 ms                                                | 97.0 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                  |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.35 ms: 1.35x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                                   |
| json_loads           | 26.5 us                                                | 24.4 us: 1.08x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                   |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                                  |
| pickle_dict          | 31.1 us                                                | 30.0 us: 1.04x faster                                                  |
| pickle_list          | 4.11 us                                                | 3.99 us: 1.03x faster                                                  |
| pickle               | 10.1 us                                                | 9.86 us: 1.02x faster                                                  |
| xml_etree_process    | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                  |
| unpickle_list        | 4.91 us                                                | 4.88 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.54 ms: 1.00x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.11 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                  |
| mako            | 10.1 ms                                                | 9.71 ms: 1.04x faster                                                  |
| genshi_text     | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                  |
| django_template | 32.6 ms                                                | 31.9 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.82x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.35 ms: 1.35x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.17 ms: 1.16x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                   |
| logging_silent          | 101 ns                                                 | 89.4 ns: 1.13x faster                                                  |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                  |
| richards                | 45.7 ms                                                | 41.2 ms: 1.11x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.11x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 997 us: 1.10x faster                                                   |
| deepcopy_memo           | 37.0 us                                                | 33.7 us: 1.10x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                                   |
| json_loads              | 26.5 us                                                | 24.4 us: 1.08x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.15 ms: 1.08x faster                                                  |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                 |
| float                   | 77.2 ms                                                | 71.7 ms: 1.08x faster                                                  |
| logging_format          | 6.68 us                                                | 6.22 us: 1.08x faster                                                  |
| nqueens                 | 83.4 ms                                                | 77.8 ms: 1.07x faster                                                  |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.66 us: 1.07x faster                                                  |
| raytrace                | 297 ms                                                 | 279 ms: 1.06x faster                                                   |
| docutils                | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                 |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                   |
| telco                   | 6.58 ms                                                | 6.22 ms: 1.06x faster                                                  |
| spectral_norm           | 100 ms                                                 | 94.5 ms: 1.06x faster                                                  |
| pprint_safe_repr        | 701 ms                                                 | 663 ms: 1.06x faster                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 64.3 ms: 1.06x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                 |
| hexiom                  | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 778 us: 1.05x faster                                                   |
| json                    | 4.94 ms                                                | 4.69 ms: 1.05x faster                                                  |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                   |
| async_generators        | 368 ms                                                 | 351 ms: 1.05x faster                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                                  |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                   |
| pyflate                 | 418 ms                                                 | 401 ms: 1.04x faster                                                   |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                                  |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                   |
| deepcopy                | 342 us                                                 | 329 us: 1.04x faster                                                   |
| mako                    | 10.1 ms                                                | 9.71 ms: 1.04x faster                                                  |
| pickle_dict             | 31.1 us                                                | 30.0 us: 1.04x faster                                                  |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                                  |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.25 ms: 1.04x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.04x faster                                                  |
| coroutines              | 25.5 ms                                                | 24.6 ms: 1.03x faster                                                  |
| tornado_http            | 96.3 ms                                                | 93.2 ms: 1.03x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                  |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                   |
| pickle_list             | 4.11 us                                                | 3.99 us: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| coverage                | 100 ms                                                 | 97.7 ms: 1.02x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.2 ms: 1.02x faster                                                  |
| django_template         | 32.6 ms                                                | 31.9 ms: 1.02x faster                                                  |
| pickle                  | 10.1 us                                                | 9.86 us: 1.02x faster                                                  |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                   |
| regex_v8                | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                  |
| chaos                   | 69.2 ms                                                | 68.0 ms: 1.02x faster                                                  |
| async_tree_memoization  | 627 ms                                                 | 617 ms: 1.02x faster                                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.68 ms: 1.02x faster                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.91 us: 1.01x faster                                                  |
| thrift                  | 756 us                                                 | 749 us: 1.01x faster                                                   |
| xml_etree_process       | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                  |
| unpickle_list           | 4.91 us                                                | 4.88 us: 1.01x faster                                                  |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                   |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| python_startup          | 8.52 ms                                                | 8.54 ms: 1.00x slower                                                  |
| gc_traversal            | 4.02 ms                                                | 4.05 ms: 1.01x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.11 ms: 1.02x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.03x slower                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                   |
| generators              | 73.5 ms                                                | 75.7 ms: 1.03x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 44.5 ns: 1.03x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.03x slower                                                  |
| nbody                   | 93.1 ms                                                | 97.0 ms: 1.04x slower                                                  |
| dask                    | 360 ms                                                 | 494 ms: 1.37x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (7): djangocms, async_tree_none, async_tree_cpu_io_mixed, sqlglot_parse, bench_mp_pool, crypto_pyaes, xml_etree_generate
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230113-3.12.0a4+-e5bd5ad/bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
