
# Results vs. 3.11.0

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: d83af14
- commit date: 2023-02-23
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                 |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                               |
| html5lib       | 64.8 ms                                                | 61.2 ms: 1.06x faster                                                |
| tornado_http   | 96.5 ms                                                | 94.5 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                 |
| nbody          | 90.0 ms                                                | 95.4 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 132 ms: 1.03x faster                                                 |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.02x faster                                                |
| regex_dna      | 203 ms                                                 | 199 ms: 1.02x faster                                                 |
| regex_effbot   | 3.46 ms                                                | 3.58 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.44 ms: 1.31x faster                                                |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                 |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                                 |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 98.8 ms: 1.05x faster                                                |
| pickle_list          | 4.14 us                                                | 4.03 us: 1.03x faster                                                |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                                |
| unpickle_list        | 4.99 us                                                | 5.08 us: 1.02x slower                                                |
| xml_etree_process    | 53.7 ms                                                | 55.0 ms: 1.03x slower                                                |
| xml_etree_generate   | 75.9 ms                                                | 80.0 ms: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.99 ms: 1.05x slower                                                |
| python_startup_no_site | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                |
| mako            | 9.83 ms                                                | 9.90 ms: 1.01x slower                                                |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                                |
| asyncio_tcp             | 883 ms                                                 | 503 ms: 1.76x faster                                                 |
| json_dumps              | 12.4 ms                                                | 9.44 ms: 1.31x faster                                                |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                 |
| deltablue               | 3.66 ms                                                | 3.15 ms: 1.16x faster                                                |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                 |
| coroutines              | 26.2 ms                                                | 23.0 ms: 1.14x faster                                                |
| richards                | 46.1 ms                                                | 41.2 ms: 1.12x faster                                                |
| genshi_xml              | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                                 |
| pycparser               | 1.19 sec                                               | 1.08 sec: 1.09x faster                                               |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                 |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                 |
| logging_silent          | 98.0 ns                                                | 91.2 ns: 1.07x faster                                                |
| json                    | 4.87 ms                                                | 4.56 ms: 1.07x faster                                                |
| mdp                     | 2.63 sec                                               | 2.48 sec: 1.06x faster                                               |
| html5lib                | 64.8 ms                                                | 61.2 ms: 1.06x faster                                                |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 98.8 ms: 1.05x faster                                                |
| fannkuch                | 384 ms                                                 | 365 ms: 1.05x faster                                                 |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                 |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                 |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                               |
| nqueens                 | 83.8 ms                                                | 80.1 ms: 1.05x faster                                                |
| hexiom                  | 6.34 ms                                                | 6.07 ms: 1.05x faster                                                |
| crypto_pyaes            | 75.7 ms                                                | 72.5 ms: 1.04x faster                                                |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                 |
| coverage                | 99.3 ms                                                | 95.0 ms: 1.04x faster                                                |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.04x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                 |
| sqlglot_optimize        | 52.7 ms                                                | 50.5 ms: 1.04x faster                                                |
| float                   | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                |
| gc_traversal            | 3.82 ms                                                | 3.67 ms: 1.04x faster                                                |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                |
| logging_simple          | 6.02 us                                                | 5.79 us: 1.04x faster                                                |
| spectral_norm           | 98.1 ms                                                | 94.5 ms: 1.04x faster                                                |
| bench_thread_pool       | 817 us                                                 | 788 us: 1.04x faster                                                 |
| deepcopy_memo           | 35.8 us                                                | 34.6 us: 1.04x faster                                                |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                                 |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                 |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                               |
| regex_compile           | 136 ms                                                 | 132 ms: 1.03x faster                                                 |
| pickle_list             | 4.14 us                                                | 4.03 us: 1.03x faster                                                |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                |
| pyflate                 | 419 ms                                                 | 408 ms: 1.03x faster                                                 |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.02x faster                                                |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                 |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.02x faster                                                |
| logging_format          | 6.48 us                                                | 6.33 us: 1.02x faster                                                |
| tornado_http            | 96.5 ms                                                | 94.5 ms: 1.02x faster                                                |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.02x faster                                                 |
| scimark_fft             | 325 ms                                                 | 319 ms: 1.02x faster                                                 |
| deepcopy                | 341 us                                                 | 334 us: 1.02x faster                                                 |
| regex_dna               | 203 ms                                                 | 199 ms: 1.02x faster                                                 |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                                 |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                |
| chaos                   | 68.7 ms                                                | 67.6 ms: 1.02x faster                                                |
| scimark_monte_carlo     | 68.0 ms                                                | 66.9 ms: 1.02x faster                                                |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                                |
| unpack_sequence         | 44.5 ns                                                | 44.3 ns: 1.01x faster                                                |
| mako                    | 9.83 ms                                                | 9.90 ms: 1.01x slower                                                |
| thrift                  | 760 us                                                 | 768 us: 1.01x slower                                                 |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                 |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.67 ms: 1.02x slower                                                |
| unpickle_list           | 4.99 us                                                | 5.08 us: 1.02x slower                                                |
| xml_etree_process       | 53.7 ms                                                | 55.0 ms: 1.03x slower                                                |
| regex_effbot            | 3.46 ms                                                | 3.58 ms: 1.04x slower                                                |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                |
| async_tree_memoization  | 624 ms                                                 | 654 ms: 1.05x slower                                                 |
| python_startup          | 8.58 ms                                                | 8.99 ms: 1.05x slower                                                |
| xml_etree_generate      | 75.9 ms                                                | 80.0 ms: 1.05x slower                                                |
| nbody                   | 90.0 ms                                                | 95.4 ms: 1.06x slower                                                |
| sqlite_synth            | 2.48 us                                                | 2.64 us: 1.06x slower                                                |
| python_startup_no_site  | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                |
| async_generators        | 356 ms                                                 | 408 ms: 1.15x slower                                                 |
| dask                    | 365 ms                                                 | 500 ms: 1.37x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (11): djangocms, async_tree_io, deepcopy_reduce, async_tree_none, sympy_sum, pickle, bench_mp_pool, chameleon, telco, unpickle, async_tree_cpu_io_mixed
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
