
# Results vs. 3.11.0

- fork: python
- ref: 72f00f420afaba3bc873
- machine: darwin-arm64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.00x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 182 ms: 1.13x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.71 ms: 1.03x slower                                                 |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| html5lib       | 34.7 ms                                                | 35.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 63.9 ms: 1.02x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| float          | 53.0 ms                                                | 55.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| regex_compile  | 76.7 ms                                                | 77.4 ms: 1.01x slower                                                 |
| regex_v8       | 16.2 ms                                                | 16.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 65.3 ms: 1.06x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.71 us: 1.04x faster                                                 |
| xml_etree_process    | 35.2 ms                                                | 34.7 ms: 1.02x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 48.2 ms: 1.01x faster                                                 |
| json_dumps           | 7.72 ms                                                | 7.63 ms: 1.01x faster                                                 |
| pickle               | 7.17 us                                                | 7.12 us: 1.01x faster                                                 |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| unpickle             | 9.70 us                                                | 9.96 us: 1.03x slower                                                 |
| unpickle_list        | 2.63 us                                                | 2.71 us: 1.03x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 175 us: 1.10x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 223 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.20 ms: 1.29x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.15 ms: 1.26x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.38 ms: 1.01x faster                                                 |
| django_template | 21.0 ms                                                | 21.0 ms: 1.00x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 31.3 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                | 27.8 ms                                                | 20.6 ms: 1.34x faster                                                 |
| python_startup_no_site | 9.31 ms                                                | 7.20 ms: 1.29x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.15 ms: 1.26x faster                                                 |
| scimark_sor            | 83.0 ms                                                | 75.5 ms: 1.10x faster                                                 |
| regex_effbot           | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                 |
| xml_etree_parse        | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| xml_etree_iterparse    | 69.2 ms                                                | 65.3 ms: 1.06x faster                                                 |
| bench_mp_pool          | 43.2 ms                                                | 41.0 ms: 1.05x faster                                                 |
| nqueens                | 61.8 ms                                                | 58.7 ms: 1.05x faster                                                 |
| sympy_sum              | 86.0 ms                                                | 82.2 ms: 1.05x faster                                                 |
| generators             | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                 |
| unpack_sequence        | 33.6 ns                                                | 32.2 ns: 1.04x faster                                                 |
| pickle_dict            | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| logging_silent         | 68.0 ns                                                | 65.4 ns: 1.04x faster                                                 |
| pickle_list            | 2.81 us                                                | 2.71 us: 1.04x faster                                                 |
| pylint                 | 271 ms                                                 | 263 ms: 1.03x faster                                                  |
| nbody                  | 65.5 ms                                                | 63.9 ms: 1.02x faster                                                 |
| bench_thread_pool      | 473 us                                                 | 462 us: 1.02x faster                                                  |
| sqlalchemy_declarative | 62.7 ms                                                | 61.5 ms: 1.02x faster                                                 |
| coroutines             | 17.7 ms                                                | 17.4 ms: 1.02x faster                                                 |
| xml_etree_process      | 35.2 ms                                                | 34.7 ms: 1.02x faster                                                 |
| regex_dna              | 152 ms                                                 | 149 ms: 1.02x faster                                                  |
| dulwich_log            | 29.9 ms                                                | 29.4 ms: 1.01x faster                                                 |
| xml_etree_generate     | 48.8 ms                                                | 48.2 ms: 1.01x faster                                                 |
| mako                   | 8.49 ms                                                | 8.38 ms: 1.01x faster                                                 |
| go                     | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| logging_simple         | 3.50 us                                                | 3.46 us: 1.01x faster                                                 |
| json_dumps             | 7.72 ms                                                | 7.63 ms: 1.01x faster                                                 |
| logging_format         | 3.78 us                                                | 3.74 us: 1.01x faster                                                 |
| sympy_str              | 152 ms                                                 | 150 ms: 1.01x faster                                                  |
| scimark_lu             | 72.1 ms                                                | 71.4 ms: 1.01x faster                                                 |
| sqlglot_normalize      | 171 ms                                                 | 170 ms: 1.01x faster                                                  |
| mdp                    | 1.54 sec                                               | 1.53 sec: 1.01x faster                                                |
| spectral_norm          | 72.8 ms                                                | 72.2 ms: 1.01x faster                                                 |
| sqlalchemy_imperative  | 7.31 ms                                                | 7.26 ms: 1.01x faster                                                 |
| docutils               | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| hexiom                 | 4.73 ms                                                | 4.70 ms: 1.01x faster                                                 |
| pickle                 | 7.17 us                                                | 7.12 us: 1.01x faster                                                 |
| async_tree_io          | 706 ms                                                 | 702 ms: 1.01x faster                                                  |
| django_template        | 21.0 ms                                                | 21.0 ms: 1.00x faster                                                 |
| crypto_pyaes           | 51.7 ms                                                | 51.6 ms: 1.00x faster                                                 |
| chaos                  | 49.5 ms                                                | 49.4 ms: 1.00x faster                                                 |
| fannkuch               | 261 ms                                                 | 260 ms: 1.00x faster                                                  |
| scimark_fft            | 199 ms                                                 | 200 ms: 1.00x slower                                                  |
| sympy_integrate        | 11.5 ms                                                | 11.5 ms: 1.01x slower                                                 |
| telco                  | 3.39 ms                                                | 3.41 ms: 1.01x slower                                                 |
| pidigits               | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| thrift                 | 433 us                                                 | 437 us: 1.01x slower                                                  |
| async_tree_none        | 285 ms                                                 | 287 ms: 1.01x slower                                                  |
| sqlglot_optimize       | 31.2 ms                                                | 31.4 ms: 1.01x slower                                                 |
| regex_compile          | 76.7 ms                                                | 77.4 ms: 1.01x slower                                                 |
| genshi_text            | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| deltablue              | 2.81 ms                                                | 2.84 ms: 1.01x slower                                                 |
| raytrace               | 207 ms                                                 | 210 ms: 1.01x slower                                                  |
| async_generators       | 195 ms                                                 | 198 ms: 1.01x slower                                                  |
| json_loads             | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| pyflate                | 311 ms                                                 | 316 ms: 1.02x slower                                                  |
| unpickle               | 9.70 us                                                | 9.96 us: 1.03x slower                                                 |
| regex_v8               | 16.2 ms                                                | 16.6 ms: 1.03x slower                                                 |
| chameleon              | 4.57 ms                                                | 4.71 ms: 1.03x slower                                                 |
| unpickle_list          | 2.63 us                                                | 2.71 us: 1.03x slower                                                 |
| html5lib               | 34.7 ms                                                | 35.9 ms: 1.03x slower                                                 |
| float                  | 53.0 ms                                                | 55.0 ms: 1.04x slower                                                 |
| richards               | 32.2 ms                                                | 33.5 ms: 1.04x slower                                                 |
| meteor_contest         | 73.8 ms                                                | 77.4 ms: 1.05x slower                                                 |
| scimark_monte_carlo    | 46.4 ms                                                | 48.7 ms: 1.05x slower                                                 |
| json                   | 2.77 ms                                                | 2.92 ms: 1.05x slower                                                 |
| genshi_xml             | 29.8 ms                                                | 31.3 ms: 1.05x slower                                                 |
| pprint_safe_repr       | 465 ms                                                 | 490 ms: 1.05x slower                                                  |
| pprint_pformat         | 950 ms                                                 | 1.01 sec: 1.06x slower                                                |
| sqlite_synth           | 1.27 us                                                | 1.35 us: 1.06x slower                                                 |
| deepcopy               | 224 us                                                 | 239 us: 1.07x slower                                                  |
| deepcopy_reduce        | 1.91 us                                                | 2.05 us: 1.07x slower                                                 |
| deepcopy_memo          | 26.3 us                                                | 28.5 us: 1.08x slower                                                 |
| unpickle_pure_python   | 159 us                                                 | 175 us: 1.10x slower                                                  |
| pickle_pure_python     | 199 us                                                 | 223 us: 1.12x slower                                                  |
| 2to3                   | 161 ms                                                 | 182 ms: 1.13x slower                                                  |
| sqlglot_transpile      | 1.12 ms                                                | 1.35 ms: 1.20x slower                                                 |
| sqlglot_parse          | 957 us                                                 | 1.19 ms: 1.24x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (8): tornado_http, aiohttp, gunicorn, sympy_expand, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, pycparser, async_tree_memoization
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, flaskblogging, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220530-3.11.0b2-72f00f4/bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4.json: mypy
