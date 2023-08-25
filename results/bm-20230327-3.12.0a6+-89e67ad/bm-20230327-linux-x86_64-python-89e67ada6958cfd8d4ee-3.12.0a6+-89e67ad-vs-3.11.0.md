
# Results vs. 3.11.0

- fork: python
- ref: 89e67ada6958cfd8d4ee
- machine: linux-x86_64
- commit hash: 89e67ad
- commit date: 2023-03-27
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                 |
| html5lib       | 64.5 ms                                                | 62.0 ms: 1.04x faster                                                  |
| tornado_http   | 96.3 ms                                                | 91.2 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.3 ms: 1.07x faster                                                  |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                   |
| float          | 77.2 ms                                                | 73.4 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                  |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.52 ms: 1.32x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                                   |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                   |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                                  |
| pickle_dict          | 31.1 us                                                | 31.2 us: 1.00x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.15 us: 1.01x slower                                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.04x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.80 ms: 1.03x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                  |
| mako            | 10.1 ms                                                | 9.95 ms: 1.01x faster                                                  |
| genshi_text     | 21.6 ms                                                | 21.8 ms: 1.01x slower                                                  |
| django_template | 32.6 ms                                                | 33.1 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 28.9 ms: 2.55x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 502 ms: 1.83x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.52 ms: 1.32x faster                                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                                   |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.11x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 33.6 us: 1.10x faster                                                  |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.67 ms: 1.10x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                  |
| spectral_norm           | 100 ms                                                 | 91.8 ms: 1.09x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                  |
| logging_silent          | 101 ns                                                 | 94.5 ns: 1.07x faster                                                  |
| nbody                   | 93.1 ms                                                | 87.3 ms: 1.07x faster                                                  |
| json                    | 4.94 ms                                                | 4.64 ms: 1.06x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                   |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.06x faster                                                   |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                 |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                                   |
| hexiom                  | 6.37 ms                                                | 6.02 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.25 ms: 1.06x faster                                                  |
| tornado_http            | 96.3 ms                                                | 91.2 ms: 1.06x faster                                                  |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                   |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                   |
| float                   | 77.2 ms                                                | 73.4 ms: 1.05x faster                                                  |
| richards                | 45.7 ms                                                | 43.5 ms: 1.05x faster                                                  |
| logging_format          | 6.68 us                                                | 6.37 us: 1.05x faster                                                  |
| scimark_fft             | 328 ms                                                 | 313 ms: 1.05x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                                 |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                                   |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                 |
| html5lib                | 64.5 ms                                                | 62.0 ms: 1.04x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 788 us: 1.04x faster                                                   |
| chaos                   | 69.2 ms                                                | 66.7 ms: 1.04x faster                                                  |
| nqueens                 | 83.4 ms                                                | 80.4 ms: 1.04x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                  |
| coverage                | 100 ms                                                 | 96.7 ms: 1.03x faster                                                  |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                   |
| unpack_sequence         | 43.1 ns                                                | 41.8 ns: 1.03x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                                  |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                                  |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                  |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.5 ms: 1.02x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                 |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                   |
| crypto_pyaes            | 74.7 ms                                                | 73.6 ms: 1.01x faster                                                  |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.01x faster                                                   |
| mako                    | 10.1 ms                                                | 9.95 ms: 1.01x faster                                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                  |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                                   |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| dulwich_log             | 63.7 ms                                                | 63.1 ms: 1.01x faster                                                  |
| pprint_safe_repr        | 701 ms                                                 | 696 ms: 1.01x faster                                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                                  |
| pickle_dict             | 31.1 us                                                | 31.2 us: 1.00x slower                                                  |
| genshi_text             | 21.6 ms                                                | 21.8 ms: 1.01x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.15 us: 1.01x slower                                                  |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.01x slower                                                  |
| django_template         | 32.6 ms                                                | 33.1 ms: 1.01x slower                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 69.1 ms: 1.02x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                  |
| thrift                  | 756 us                                                 | 781 us: 1.03x slower                                                   |
| python_startup          | 8.52 ms                                                | 8.80 ms: 1.03x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.08 us: 1.04x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                                   |
| comprehensions          | 22.4 us                                                | 23.8 us: 1.06x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                  |
| async_generators        | 368 ms                                                 | 410 ms: 1.11x slower                                                   |
| dask                    | 360 ms                                                 | 510 ms: 1.42x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (10): go, async_tree_none, regex_dna, chameleon, async_tree_io, async_tree_cpu_io_mixed, pyflate, bench_mp_pool, scimark_lu, djangocms
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
