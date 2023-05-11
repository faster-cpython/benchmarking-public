
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: darwin-arm64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.21x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 202 ms: 1.25x slower                                   |
| chameleon      | 4.60 ms                                                | 5.84 ms: 1.27x slower                                  |
| docutils       | 1.47 sec                                               | 1.78 sec: 1.21x slower                                 |
| html5lib       | 34.7 ms                                                | 44.1 ms: 1.27x slower                                  |
| tornado_http   | 71.5 ms                                                | 91.9 ms: 1.29x slower                                  |
| Geometric mean | (ref)                                                  | 1.26x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| float          | 53.0 ms                                                | 72.3 ms: 1.37x slower                                  |
| nbody          | 65.6 ms                                                | 94.1 ms: 1.44x slower                                  |
| Geometric mean | (ref)                                                  | 1.25x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.08x faster                                  |
| regex_dna      | 152 ms                                                 | 160 ms: 1.05x slower                                   |
| regex_v8       | 16.1 ms                                                | 17.5 ms: 1.09x slower                                  |
| regex_compile  | 76.7 ms                                                | 96.6 ms: 1.26x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_dict          | 18.0 us                                                | 17.8 us: 1.01x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                   |
| unpickle_list        | 2.65 us                                                | 2.66 us: 1.01x slower                                  |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| unpickle             | 9.67 us                                                | 9.77 us: 1.01x slower                                  |
| pickle               | 7.15 us                                                | 7.36 us: 1.03x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 72.6 ms: 1.04x slower                                  |
| json_loads           | 16.1 us                                                | 16.9 us: 1.05x slower                                  |
| json_dumps           | 7.63 ms                                                | 8.38 ms: 1.10x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 54.3 ms: 1.12x slower                                  |
| tomli_loads          | 1.47 sec                                               | 1.76 sec: 1.20x slower                                 |
| unpickle_pure_python | 159 us                                                 | 203 us: 1.28x slower                                   |
| xml_etree_process    | 35.1 ms                                                | 45.1 ms: 1.28x slower                                  |
| pickle_pure_python   | 201 us                                                 | 284 us: 1.41x slower                                   |
| Geometric mean       | (ref)                                                  | 1.10x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.73 ms: 1.05x faster                                  |
| python_startup         | 12.4 ms                                                | 12.6 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 18.4 ms: 1.20x slower                                  |
| mako            | 8.53 ms                                                | 10.5 ms: 1.23x slower                                  |
| genshi_xml      | 29.8 ms                                                | 37.6 ms: 1.26x slower                                  |
| django_template | 21.0 ms                                                | 27.3 ms: 1.30x slower                                  |
| Geometric mean  | (ref)                                                  | 1.25x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| coverage                 | 58.4 ms                                                | 40.8 ms: 1.43x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.45 ms: 1.08x faster                                  |
| bench_mp_pool            | 43.9 ms                                                | 41.0 ms: 1.07x faster                                  |
| python_startup_no_site   | 10.2 ms                                                | 9.73 ms: 1.05x faster                                  |
| pickle_dict              | 18.0 us                                                | 17.8 us: 1.01x faster                                  |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                  |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                   |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| unpickle_list            | 2.65 us                                                | 2.66 us: 1.01x slower                                  |
| pickle_list              | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| unpickle                 | 9.67 us                                                | 9.77 us: 1.01x slower                                  |
| python_startup           | 12.4 ms                                                | 12.6 ms: 1.01x slower                                  |
| typing_runtime_protocols | 336 us                                                 | 344 us: 1.02x slower                                   |
| pickle                   | 7.15 us                                                | 7.36 us: 1.03x slower                                  |
| asyncio_tcp              | 651 ms                                                 | 673 ms: 1.03x slower                                   |
| xml_etree_iterparse      | 70.1 ms                                                | 72.6 ms: 1.04x slower                                  |
| json_loads               | 16.1 us                                                | 16.9 us: 1.05x slower                                  |
| regex_dna                | 152 ms                                                 | 160 ms: 1.05x slower                                   |
| pathlib                  | 27.2 ms                                                | 28.8 ms: 1.06x slower                                  |
| meteor_contest           | 73.5 ms                                                | 78.6 ms: 1.07x slower                                  |
| mdp                      | 1.55 sec                                               | 1.67 sec: 1.08x slower                                 |
| telco                    | 3.41 ms                                                | 3.68 ms: 1.08x slower                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.47 ms: 1.09x slower                                  |
| regex_v8                 | 16.1 ms                                                | 17.5 ms: 1.09x slower                                  |
| comprehensions           | 16.1 us                                                | 17.7 us: 1.10x slower                                  |
| json_dumps               | 7.63 ms                                                | 8.38 ms: 1.10x slower                                  |
| sympy_sum                | 85.5 ms                                                | 94.3 ms: 1.10x slower                                  |
| json                     | 2.78 ms                                                | 3.10 ms: 1.12x slower                                  |
| sympy_str                | 151 ms                                                 | 169 ms: 1.12x slower                                   |
| xml_etree_generate       | 48.3 ms                                                | 54.3 ms: 1.12x slower                                  |
| flaskblogging            | 2.43 ms                                                | 2.75 ms: 1.13x slower                                  |
| pylint                   | 272 ms                                                 | 307 ms: 1.13x slower                                   |
| unpack_sequence          | 34.1 ns                                                | 38.7 ns: 1.13x slower                                  |
| coroutines               | 17.8 ms                                                | 20.2 ms: 1.14x slower                                  |
| sympy_expand             | 242 ms                                                 | 276 ms: 1.14x slower                                   |
| nqueens                  | 59.8 ms                                                | 68.1 ms: 1.14x slower                                  |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.64 sec: 1.14x slower                                 |
| generators               | 28.8 ms                                                | 32.9 ms: 1.15x slower                                  |
| sqlglot_normalize        | 171 ms                                                 | 197 ms: 1.15x slower                                   |
| bench_thread_pool        | 474 us                                                 | 548 us: 1.16x slower                                   |
| sqlite_synth             | 1.27 us                                                | 1.47 us: 1.16x slower                                  |
| sympy_integrate          | 11.5 ms                                                | 13.4 ms: 1.16x slower                                  |
| scimark_fft              | 200 ms                                                 | 232 ms: 1.16x slower                                   |
| async_generators         | 196 ms                                                 | 233 ms: 1.19x slower                                   |
| sqlalchemy_declarative   | 62.6 ms                                                | 74.8 ms: 1.20x slower                                  |
| tomli_loads              | 1.47 sec                                               | 1.76 sec: 1.20x slower                                 |
| gunicorn                 | 1.11 ms                                                | 1.34 ms: 1.20x slower                                  |
| genshi_text              | 15.3 ms                                                | 18.4 ms: 1.20x slower                                  |
| docutils                 | 1.47 sec                                               | 1.78 sec: 1.21x slower                                 |
| fannkuch                 | 261 ms                                                 | 317 ms: 1.21x slower                                   |
| sqlglot_optimize         | 31.1 ms                                                | 38.0 ms: 1.22x slower                                  |
| dulwich_log              | 30.3 ms                                                | 37.1 ms: 1.22x slower                                  |
| create_gc_cycles         | 716 us                                                 | 876 us: 1.22x slower                                   |
| mako                     | 8.53 ms                                                | 10.5 ms: 1.23x slower                                  |
| aiohttp                  | 1.05 ms                                                | 1.29 ms: 1.23x slower                                  |
| deepcopy                 | 223 us                                                 | 278 us: 1.25x slower                                   |
| deepcopy_reduce          | 1.91 us                                                | 2.38 us: 1.25x slower                                  |
| sqlalchemy_imperative    | 7.20 ms                                                | 9.03 ms: 1.25x slower                                  |
| 2to3                     | 161 ms                                                 | 202 ms: 1.25x slower                                   |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 670 ms: 1.26x slower                                   |
| regex_compile            | 76.7 ms                                                | 96.6 ms: 1.26x slower                                  |
| genshi_xml               | 29.8 ms                                                | 37.6 ms: 1.26x slower                                  |
| chameleon                | 4.60 ms                                                | 5.84 ms: 1.27x slower                                  |
| html5lib                 | 34.7 ms                                                | 44.1 ms: 1.27x slower                                  |
| unpickle_pure_python     | 159 us                                                 | 203 us: 1.28x slower                                   |
| xml_etree_process        | 35.1 ms                                                | 45.1 ms: 1.28x slower                                  |
| tornado_http             | 71.5 ms                                                | 91.9 ms: 1.29x slower                                  |
| django_template          | 21.0 ms                                                | 27.3 ms: 1.30x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.24 sec: 1.30x slower                                 |
| logging_simple           | 3.55 us                                                | 4.63 us: 1.30x slower                                  |
| pprint_safe_repr         | 466 ms                                                 | 609 ms: 1.30x slower                                   |
| deepcopy_memo            | 26.3 us                                                | 34.5 us: 1.31x slower                                  |
| pycparser                | 698 ms                                                 | 915 ms: 1.31x slower                                   |
| logging_format           | 3.78 us                                                | 5.01 us: 1.33x slower                                  |
| thrift                   | 442 us                                                 | 586 us: 1.33x slower                                   |
| spectral_norm            | 72.6 ms                                                | 96.4 ms: 1.33x slower                                  |
| hexiom                   | 4.72 ms                                                | 6.32 ms: 1.34x slower                                  |
| chaos                    | 49.4 ms                                                | 66.8 ms: 1.35x slower                                  |
| float                    | 53.0 ms                                                | 72.3 ms: 1.37x slower                                  |
| sqlglot_transpile        | 1.12 ms                                                | 1.54 ms: 1.37x slower                                  |
| sqlglot_parse            | 959 us                                                 | 1.33 ms: 1.39x slower                                  |
| async_tree_none          | 286 ms                                                 | 402 ms: 1.41x slower                                   |
| pickle_pure_python       | 201 us                                                 | 284 us: 1.41x slower                                   |
| nbody                    | 65.6 ms                                                | 94.1 ms: 1.44x slower                                  |
| async_tree_io            | 704 ms                                                 | 1.02 sec: 1.45x slower                                 |
| pyflate                  | 310 ms                                                 | 453 ms: 1.46x slower                                   |
| async_tree_memoization   | 336 ms                                                 | 493 ms: 1.47x slower                                   |
| scimark_lu               | 73.3 ms                                                | 110 ms: 1.50x slower                                   |
| crypto_pyaes             | 51.7 ms                                                | 78.0 ms: 1.51x slower                                  |
| go                       | 109 ms                                                 | 165 ms: 1.52x slower                                   |
| scimark_sor              | 82.6 ms                                                | 127 ms: 1.53x slower                                   |
| richards_super           | 39.2 ms                                                | 60.7 ms: 1.55x slower                                  |
| scimark_monte_carlo      | 46.5 ms                                                | 72.2 ms: 1.55x slower                                  |
| mypy2                    | 195 ms                                                 | 308 ms: 1.58x slower                                   |
| raytrace                 | 207 ms                                                 | 328 ms: 1.58x slower                                   |
| richards                 | 32.2 ms                                                | 51.4 ms: 1.59x slower                                  |
| logging_silent           | 68.1 ns                                                | 119 ns: 1.75x slower                                   |
| deltablue                | 2.81 ms                                                | 5.15 ms: 1.83x slower                                  |
| Geometric mean           | (ref)                                                  | 1.21x slower                                           |
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: dask
