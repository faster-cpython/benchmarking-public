
# Results vs. 3.11.0

- fork: python
- ref: d1a89ce5156cd4e1eff5
- machine: linux-x86_64
- commit hash: d1a89ce
- commit date: 2023-03-21
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.35 ms: 1.02x faster                                                  |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                 |
| html5lib       | 64.5 ms                                                | 60.5 ms: 1.07x faster                                                  |
| tornado_http   | 96.3 ms                                                | 91.0 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.7 ms: 1.06x faster                                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| float          | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.42 ms: 1.17x faster                                                  |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.59 ms: 1.31x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                   |
| json_loads           | 26.5 us                                                | 24.2 us: 1.10x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 151 ms: 1.05x faster                                                   |
| unpickle             | 13.7 us                                                | 13.2 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| pickle_dict          | 31.1 us                                                | 31.2 us: 1.00x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.05 us: 1.03x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.23 us: 1.03x slower                                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.88 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.56 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                  |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.7 ms: 2.47x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.59 ms: 1.31x faster                                                  |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.42 ms: 1.17x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.17 ms: 1.16x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                   |
| coroutines              | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                  |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                   |
| json_loads              | 26.5 us                                                | 24.2 us: 1.10x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                  |
| spectral_norm           | 100 ms                                                 | 92.0 ms: 1.09x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                  |
| scimark_fft             | 328 ms                                                 | 303 ms: 1.08x faster                                                   |
| json                    | 4.94 ms                                                | 4.57 ms: 1.08x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                                   |
| logging_simple          | 6.03 us                                                | 5.62 us: 1.07x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 34.5 us: 1.07x faster                                                  |
| coverage                | 100 ms                                                 | 93.4 ms: 1.07x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.07x faster                                                 |
| logging_format          | 6.68 us                                                | 6.26 us: 1.07x faster                                                  |
| html5lib                | 64.5 ms                                                | 60.5 ms: 1.07x faster                                                  |
| logging_silent          | 101 ns                                                 | 94.8 ns: 1.07x faster                                                  |
| nbody                   | 93.1 ms                                                | 87.7 ms: 1.06x faster                                                  |
| richards                | 45.7 ms                                                | 43.2 ms: 1.06x faster                                                  |
| tornado_http            | 96.3 ms                                                | 91.0 ms: 1.06x faster                                                  |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                                   |
| fannkuch                | 388 ms                                                 | 368 ms: 1.06x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 151 ms: 1.05x faster                                                   |
| chaos                   | 69.2 ms                                                | 65.8 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.28 ms: 1.05x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.84 ms: 1.05x faster                                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| nqueens                 | 83.4 ms                                                | 79.7 ms: 1.05x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.9 ms: 1.04x faster                                                  |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                   |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                   |
| bench_thread_pool       | 819 us                                                 | 788 us: 1.04x faster                                                   |
| float                   | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                 |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                 |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                   |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                   |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| hexiom                  | 6.37 ms                                                | 6.17 ms: 1.03x faster                                                  |
| unpickle                | 13.7 us                                                | 13.2 us: 1.03x faster                                                  |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 66.2 ms: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                  |
| chameleon               | 6.47 ms                                                | 6.35 ms: 1.02x faster                                                  |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 691 ms: 1.02x faster                                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.7 ms: 1.01x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                   |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                                  |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                   |
| pyflate                 | 418 ms                                                 | 416 ms: 1.01x faster                                                   |
| pickle_dict             | 31.1 us                                                | 31.2 us: 1.00x slower                                                  |
| mdp                     | 2.62 sec                                               | 2.63 sec: 1.00x slower                                                 |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                  |
| thrift                  | 756 us                                                 | 771 us: 1.02x slower                                                   |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.05 us: 1.03x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.23 us: 1.03x slower                                                  |
| unpack_sequence         | 43.1 ns                                                | 44.4 ns: 1.03x slower                                                  |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                  |
| python_startup          | 8.52 ms                                                | 8.88 ms: 1.04x slower                                                  |
| comprehensions          | 22.4 us                                                | 23.4 us: 1.04x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.56 ms: 1.09x slower                                                  |
| async_generators        | 368 ms                                                 | 417 ms: 1.13x slower                                                   |
| dask                    | 360 ms                                                 | 501 ms: 1.39x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, regex_v8, genshi_text, bench_mp_pool, regex_dna, async_tree_io, mako, djangocms, create_gc_cycles, telco, crypto_pyaes, deepcopy_reduce
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
