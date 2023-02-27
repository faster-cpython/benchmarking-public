
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d71edbd
- commit date: 2023-02-25
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                   |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                 |
| html5lib       | 64.8 ms                                                | 61.1 ms: 1.06x faster                                  |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| float          | 76.8 ms                                                | 73.9 ms: 1.04x faster                                  |
| nbody          | 90.0 ms                                                | 96.6 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                   |
| regex_v8       | 22.2 ms                                                | 21.6 ms: 1.03x faster                                  |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                   |
| regex_effbot   | 3.46 ms                                                | 3.65 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.45 ms: 1.31x faster                                  |
| unpickle_pure_python | 227 us                                                 | 195 us: 1.17x faster                                   |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                  |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                  |
| unpickle_list        | 4.99 us                                                | 5.02 us: 1.01x slower                                  |
| pickle_list          | 4.14 us                                                | 4.19 us: 1.01x slower                                  |
| pickle_dict          | 31.2 us                                                | 31.7 us: 1.02x slower                                  |
| xml_etree_process    | 53.7 ms                                                | 55.0 ms: 1.02x slower                                  |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 80.3 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.01 ms: 1.05x slower                                  |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.3 ms: 1.11x faster                                  |
| genshi_text     | 21.5 ms                                                | 20.4 ms: 1.05x faster                                  |
| mako            | 9.83 ms                                                | 9.89 ms: 1.01x slower                                  |
| django_template | 32.3 ms                                                | 33.0 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators             | 73.5 ms                                                | 29.6 ms: 2.48x faster                                  |
| asyncio_tcp            | 883 ms                                                 | 502 ms: 1.76x faster                                   |
| json_dumps             | 12.4 ms                                                | 9.45 ms: 1.31x faster                                  |
| mypy2                  | 420 ms                                                 | 332 ms: 1.26x faster                                   |
| unpickle_pure_python   | 227 us                                                 | 195 us: 1.17x faster                                   |
| deltablue              | 3.66 ms                                                | 3.14 ms: 1.17x faster                                  |
| richards               | 46.1 ms                                                | 40.6 ms: 1.14x faster                                  |
| coroutines             | 26.2 ms                                                | 23.0 ms: 1.14x faster                                  |
| genshi_xml             | 51.4 ms                                                | 46.3 ms: 1.11x faster                                  |
| json_loads             | 26.1 us                                                | 23.9 us: 1.09x faster                                  |
| pickle_pure_python     | 308 us                                                 | 282 us: 1.09x faster                                   |
| pycparser              | 1.19 sec                                               | 1.09 sec: 1.09x faster                                 |
| scimark_sor            | 115 ms                                                 | 106 ms: 1.08x faster                                   |
| xml_etree_parse        | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| json                   | 4.87 ms                                                | 4.54 ms: 1.07x faster                                  |
| html5lib               | 64.8 ms                                                | 61.1 ms: 1.06x faster                                  |
| fannkuch               | 384 ms                                                 | 364 ms: 1.06x faster                                   |
| genshi_text            | 21.5 ms                                                | 20.4 ms: 1.05x faster                                  |
| hexiom                 | 6.34 ms                                                | 6.01 ms: 1.05x faster                                  |
| go                     | 140 ms                                                 | 133 ms: 1.05x faster                                   |
| logging_simple         | 6.02 us                                                | 5.72 us: 1.05x faster                                  |
| unpack_sequence        | 44.5 ns                                                | 42.4 ns: 1.05x faster                                  |
| xml_etree_iterparse    | 104 ms                                                 | 99.3 ms: 1.05x faster                                  |
| nqueens                | 83.8 ms                                                | 80.0 ms: 1.05x faster                                  |
| sqlglot_normalize      | 108 ms                                                 | 103 ms: 1.05x faster                                   |
| sympy_expand           | 475 ms                                                 | 454 ms: 1.05x faster                                   |
| 2to3                   | 259 ms                                                 | 248 ms: 1.05x faster                                   |
| regex_compile          | 136 ms                                                 | 131 ms: 1.04x faster                                   |
| sqlglot_optimize       | 52.7 ms                                                | 50.5 ms: 1.04x faster                                  |
| raytrace               | 291 ms                                                 | 280 ms: 1.04x faster                                   |
| pidigits               | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| aiohttp                | 1.05 ms                                                | 1.01 ms: 1.04x faster                                  |
| float                  | 76.8 ms                                                | 73.9 ms: 1.04x faster                                  |
| pprint_pformat         | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| logging_silent         | 98.0 ns                                                | 94.4 ns: 1.04x faster                                  |
| bench_thread_pool      | 817 us                                                 | 787 us: 1.04x faster                                   |
| pprint_safe_repr       | 706 ms                                                 | 681 ms: 1.04x faster                                   |
| sympy_str              | 291 ms                                                 | 282 ms: 1.03x faster                                   |
| deepcopy_memo          | 35.8 us                                                | 34.7 us: 1.03x faster                                  |
| scimark_monte_carlo    | 68.0 ms                                                | 66.0 ms: 1.03x faster                                  |
| coverage               | 99.3 ms                                                | 96.5 ms: 1.03x faster                                  |
| pyflate                | 419 ms                                                 | 407 ms: 1.03x faster                                   |
| regex_v8               | 22.2 ms                                                | 21.6 ms: 1.03x faster                                  |
| scimark_fft            | 325 ms                                                 | 317 ms: 1.03x faster                                   |
| sympy_integrate        | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| deepcopy               | 341 us                                                 | 332 us: 1.03x faster                                   |
| gunicorn               | 1.12 ms                                                | 1.09 ms: 1.03x faster                                  |
| logging_format         | 6.48 us                                                | 6.31 us: 1.03x faster                                  |
| chaos                  | 68.7 ms                                                | 67.0 ms: 1.03x faster                                  |
| tornado_http           | 96.5 ms                                                | 94.3 ms: 1.02x faster                                  |
| docutils               | 2.60 sec                                               | 2.54 sec: 1.02x faster                                 |
| pathlib                | 18.1 ms                                                | 17.7 ms: 1.02x faster                                  |
| sqlalchemy_imperative  | 18.1 ms                                                | 17.7 ms: 1.02x faster                                  |
| spectral_norm          | 98.1 ms                                                | 96.4 ms: 1.02x faster                                  |
| dulwich_log            | 64.0 ms                                                | 63.1 ms: 1.01x faster                                  |
| crypto_pyaes           | 75.7 ms                                                | 74.7 ms: 1.01x faster                                  |
| create_gc_cycles       | 1.52 ms                                                | 1.50 ms: 1.01x faster                                  |
| deepcopy_reduce        | 3.02 us                                                | 2.99 us: 1.01x faster                                  |
| meteor_contest         | 104 ms                                                 | 104 ms: 1.01x faster                                   |
| gc_traversal           | 3.82 ms                                                | 3.83 ms: 1.00x slower                                  |
| mako                   | 9.83 ms                                                | 9.89 ms: 1.01x slower                                  |
| unpickle_list          | 4.99 us                                                | 5.02 us: 1.01x slower                                  |
| pickle_list            | 4.14 us                                                | 4.19 us: 1.01x slower                                  |
| mdp                    | 2.63 sec                                               | 2.66 sec: 1.01x slower                                 |
| thrift                 | 760 us                                                 | 771 us: 1.01x slower                                   |
| pickle_dict            | 31.2 us                                                | 31.7 us: 1.02x slower                                  |
| telco                  | 6.43 ms                                                | 6.57 ms: 1.02x slower                                  |
| django_template        | 32.3 ms                                                | 33.0 ms: 1.02x slower                                  |
| regex_dna              | 203 ms                                                 | 208 ms: 1.02x slower                                   |
| async_tree_memoization | 624 ms                                                 | 640 ms: 1.02x slower                                   |
| xml_etree_process      | 53.7 ms                                                | 55.0 ms: 1.02x slower                                  |
| sqlglot_transpile      | 1.65 ms                                                | 1.70 ms: 1.03x slower                                  |
| sqlglot_parse          | 1.36 ms                                                | 1.41 ms: 1.04x slower                                  |
| python_startup         | 8.58 ms                                                | 9.01 ms: 1.05x slower                                  |
| pickle                 | 9.90 us                                                | 10.4 us: 1.05x slower                                  |
| regex_effbot           | 3.46 ms                                                | 3.65 ms: 1.06x slower                                  |
| xml_etree_generate     | 75.9 ms                                                | 80.3 ms: 1.06x slower                                  |
| sqlite_synth           | 2.48 us                                                | 2.62 us: 1.06x slower                                  |
| nbody                  | 90.0 ms                                                | 96.6 ms: 1.07x slower                                  |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                  |
| async_generators       | 356 ms                                                 | 420 ms: 1.18x slower                                   |
| dask                   | 365 ms                                                 | 499 ms: 1.37x slower                                   |
| Geometric mean         | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (11): unpickle, sqlalchemy_declarative, async_tree_io, djangocms, async_tree_none, bench_mp_pool, chameleon, sympy_sum, scimark_lu, async_tree_cpu_io_mixed, scimark_sparse_mat_mult
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
