
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: darwin-arm64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 161 ms: 1.25x faster                                   |
| chameleon      | 5.84 ms                                                | 4.60 ms: 1.27x faster                                  |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                 |
| html5lib       | 44.1 ms                                                | 34.7 ms: 1.27x faster                                  |
| tornado_http   | 91.9 ms                                                | 71.5 ms: 1.29x faster                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 65.6 ms: 1.44x faster                                  |
| float          | 72.3 ms                                                | 53.0 ms: 1.37x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 76.7 ms: 1.26x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 160 ms                                                 | 152 ms: 1.05x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.63 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 201 us: 1.41x faster                                   |
| xml_etree_process    | 45.1 ms                                                | 35.1 ms: 1.28x faster                                  |
| unpickle_pure_python | 203 us                                                 | 159 us: 1.28x faster                                   |
| tomli_loads          | 1.76 sec                                               | 1.47 sec: 1.20x faster                                 |
| xml_etree_generate   | 54.3 ms                                                | 48.3 ms: 1.12x faster                                  |
| json_dumps           | 8.38 ms                                                | 7.63 ms: 1.10x faster                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 70.1 ms: 1.04x faster                                  |
| pickle               | 7.36 us                                                | 7.15 us: 1.03x faster                                  |
| unpickle             | 9.77 us                                                | 9.67 us: 1.01x faster                                  |
| pickle_list          | 2.83 us                                                | 2.81 us: 1.01x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.65 us: 1.01x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 108 ms: 1.01x slower                                   |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.4 ms: 1.01x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 10.2 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.0 ms: 1.30x faster                                  |
| genshi_xml      | 37.6 ms                                                | 29.8 ms: 1.26x faster                                  |
| mako            | 10.5 ms                                                | 8.53 ms: 1.23x faster                                  |
| genshi_text     | 18.4 ms                                                | 15.3 ms: 1.20x faster                                  |
| Geometric mean  | (ref)                                                  | 1.25x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue                | 5.15 ms                                                | 2.81 ms: 1.83x faster                                  |
| logging_silent           | 119 ns                                                 | 68.1 ns: 1.75x faster                                  |
| richards                 | 51.4 ms                                                | 32.2 ms: 1.59x faster                                  |
| raytrace                 | 328 ms                                                 | 207 ms: 1.58x faster                                   |
| mypy2                    | 308 ms                                                 | 195 ms: 1.58x faster                                   |
| scimark_monte_carlo      | 72.2 ms                                                | 46.5 ms: 1.55x faster                                  |
| richards_super           | 60.7 ms                                                | 39.2 ms: 1.55x faster                                  |
| scimark_sor              | 127 ms                                                 | 82.6 ms: 1.53x faster                                  |
| go                       | 165 ms                                                 | 109 ms: 1.52x faster                                   |
| crypto_pyaes             | 78.0 ms                                                | 51.7 ms: 1.51x faster                                  |
| scimark_lu               | 110 ms                                                 | 73.3 ms: 1.50x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 336 ms: 1.47x faster                                   |
| pyflate                  | 453 ms                                                 | 310 ms: 1.46x faster                                   |
| async_tree_io            | 1.02 sec                                               | 704 ms: 1.45x faster                                   |
| nbody                    | 94.1 ms                                                | 65.6 ms: 1.44x faster                                  |
| pickle_pure_python       | 284 us                                                 | 201 us: 1.41x faster                                   |
| async_tree_none          | 402 ms                                                 | 286 ms: 1.41x faster                                   |
| sqlglot_parse            | 1.33 ms                                                | 959 us: 1.39x faster                                   |
| sqlglot_transpile        | 1.54 ms                                                | 1.12 ms: 1.37x faster                                  |
| float                    | 72.3 ms                                                | 53.0 ms: 1.37x faster                                  |
| chaos                    | 66.8 ms                                                | 49.4 ms: 1.35x faster                                  |
| hexiom                   | 6.32 ms                                                | 4.72 ms: 1.34x faster                                  |
| spectral_norm            | 96.4 ms                                                | 72.6 ms: 1.33x faster                                  |
| thrift                   | 586 us                                                 | 442 us: 1.33x faster                                   |
| logging_format           | 5.01 us                                                | 3.78 us: 1.33x faster                                  |
| pycparser                | 915 ms                                                 | 698 ms: 1.31x faster                                   |
| deepcopy_memo            | 34.5 us                                                | 26.3 us: 1.31x faster                                  |
| pprint_safe_repr         | 609 ms                                                 | 466 ms: 1.30x faster                                   |
| logging_simple           | 4.63 us                                                | 3.55 us: 1.30x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 954 ms: 1.30x faster                                   |
| django_template          | 27.3 ms                                                | 21.0 ms: 1.30x faster                                  |
| tornado_http             | 91.9 ms                                                | 71.5 ms: 1.29x faster                                  |
| xml_etree_process        | 45.1 ms                                                | 35.1 ms: 1.28x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 159 us: 1.28x faster                                   |
| html5lib                 | 44.1 ms                                                | 34.7 ms: 1.27x faster                                  |
| chameleon                | 5.84 ms                                                | 4.60 ms: 1.27x faster                                  |
| genshi_xml               | 37.6 ms                                                | 29.8 ms: 1.26x faster                                  |
| regex_compile            | 96.6 ms                                                | 76.7 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 533 ms: 1.26x faster                                   |
| 2to3                     | 202 ms                                                 | 161 ms: 1.25x faster                                   |
| sqlalchemy_imperative    | 9.03 ms                                                | 7.20 ms: 1.25x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 1.91 us: 1.25x faster                                  |
| deepcopy                 | 278 us                                                 | 223 us: 1.25x faster                                   |
| aiohttp                  | 1.29 ms                                                | 1.05 ms: 1.23x faster                                  |
| mako                     | 10.5 ms                                                | 8.53 ms: 1.23x faster                                  |
| create_gc_cycles         | 876 us                                                 | 716 us: 1.22x faster                                   |
| dulwich_log              | 37.1 ms                                                | 30.3 ms: 1.22x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 31.1 ms: 1.22x faster                                  |
| fannkuch                 | 317 ms                                                 | 261 ms: 1.21x faster                                   |
| docutils                 | 1.78 sec                                               | 1.47 sec: 1.21x faster                                 |
| genshi_text              | 18.4 ms                                                | 15.3 ms: 1.20x faster                                  |
| gunicorn                 | 1.34 ms                                                | 1.11 ms: 1.20x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.47 sec: 1.20x faster                                 |
| sqlalchemy_declarative   | 74.8 ms                                                | 62.6 ms: 1.20x faster                                  |
| async_generators         | 233 ms                                                 | 196 ms: 1.19x faster                                   |
| scimark_fft              | 232 ms                                                 | 200 ms: 1.16x faster                                   |
| sympy_integrate          | 13.4 ms                                                | 11.5 ms: 1.16x faster                                  |
| sqlite_synth             | 1.47 us                                                | 1.27 us: 1.16x faster                                  |
| bench_thread_pool        | 548 us                                                 | 474 us: 1.16x faster                                   |
| sqlglot_normalize        | 197 ms                                                 | 171 ms: 1.15x faster                                   |
| generators               | 32.9 ms                                                | 28.8 ms: 1.15x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.44 sec: 1.14x faster                                 |
| nqueens                  | 68.1 ms                                                | 59.8 ms: 1.14x faster                                  |
| sympy_expand             | 276 ms                                                 | 242 ms: 1.14x faster                                   |
| coroutines               | 20.2 ms                                                | 17.8 ms: 1.14x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 34.1 ns: 1.13x faster                                  |
| pylint                   | 307 ms                                                 | 272 ms: 1.13x faster                                   |
| flaskblogging            | 2.75 ms                                                | 2.43 ms: 1.13x faster                                  |
| xml_etree_generate       | 54.3 ms                                                | 48.3 ms: 1.12x faster                                  |
| sympy_str                | 169 ms                                                 | 151 ms: 1.12x faster                                   |
| json                     | 3.10 ms                                                | 2.78 ms: 1.12x faster                                  |
| sympy_sum                | 94.3 ms                                                | 85.5 ms: 1.10x faster                                  |
| json_dumps               | 8.38 ms                                                | 7.63 ms: 1.10x faster                                  |
| comprehensions           | 17.7 us                                                | 16.1 us: 1.10x faster                                  |
| regex_v8                 | 17.5 ms                                                | 16.1 ms: 1.09x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.19 ms: 1.09x faster                                  |
| telco                    | 3.68 ms                                                | 3.41 ms: 1.08x faster                                  |
| mdp                      | 1.67 sec                                               | 1.55 sec: 1.08x faster                                 |
| meteor_contest           | 78.6 ms                                                | 73.5 ms: 1.07x faster                                  |
| pathlib                  | 28.8 ms                                                | 27.2 ms: 1.06x faster                                  |
| regex_dna                | 160 ms                                                 | 152 ms: 1.05x faster                                   |
| json_loads               | 16.9 us                                                | 16.1 us: 1.05x faster                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 70.1 ms: 1.04x faster                                  |
| asyncio_tcp              | 673 ms                                                 | 651 ms: 1.03x faster                                   |
| pickle                   | 7.36 us                                                | 7.15 us: 1.03x faster                                  |
| typing_runtime_protocols | 344 us                                                 | 336 us: 1.02x faster                                   |
| python_startup           | 12.6 ms                                                | 12.4 ms: 1.01x faster                                  |
| unpickle                 | 9.77 us                                                | 9.67 us: 1.01x faster                                  |
| pickle_list              | 2.83 us                                                | 2.81 us: 1.01x faster                                  |
| unpickle_list            | 2.66 us                                                | 2.65 us: 1.01x faster                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| xml_etree_parse          | 107 ms                                                 | 108 ms: 1.01x slower                                   |
| gc_traversal             | 2.40 ms                                                | 2.42 ms: 1.01x slower                                  |
| pickle_dict              | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| python_startup_no_site   | 9.73 ms                                                | 10.2 ms: 1.05x slower                                  |
| bench_mp_pool            | 41.0 ms                                                | 43.9 ms: 1.07x slower                                  |
| regex_effbot             | 2.45 ms                                                | 2.63 ms: 1.08x slower                                  |
| coverage                 | 40.8 ms                                                | 58.4 ms: 1.43x slower                                  |
| Geometric mean           | (ref)                                                  | 1.21x faster                                           |
Ignored benchmarks (1) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: dask


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
